# *****************************************************************************
# supporters/serializers.py
# *****************************************************************************

from rest_framework import serializers

from .models import (Address, Cause, District, Supporter)

# *****************************************************************************
# DistrictSerializer
# *****************************************************************************


class DistrictSerializer(serializers.ModelSerializer):
    
    """
    A serializer to serializer District objects.

    """

    id = serializers.IntegerField(required=False)
    tag = serializers.CharField(required=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = District
        fields = (
            'id',
            'tag',
            'name'
        )


# *****************************************************************************
# AddressSerializer
# *****************************************************************************


class AddressSerializer(serializers.ModelSerializer):
    
    """
    A serializer to serializer Address objects.

    """

    id = serializers.IntegerField(required=False)
    street = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    zipcode = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    district = DistrictSerializer(required=False)

    class Meta:
        model = Address
        fields = (
            'id',
            'street',
            'city',
            'zipcode',
            'state',
            'district'
        )


# *****************************************************************************
# CauseSerializer
# *****************************************************************************


class CauseSerializer(serializers.ModelSerializer):
    
    """
    A serializer to serializer Cause objects.

    """

    id = serializers.IntegerField(required=False)
    tag = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Cause
        fields = (
            'id',
            'tag',
            'name',
            'description'
        )


# *****************************************************************************
# SupporterSeriaizer
# *****************************************************************************


class SupporterSerializer(serializers.ModelSerializer):
    
    """
    A serializer to serializer Supporter objects.

    """

    id = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    phonenumber = serializers.CharField(required=False)
    address = AddressSerializer(required=False)
    causes = CauseSerializer(required=False, many=True)

    def _get_or_create_district(self, data):
        """
        Helper method to get or create District object from
        address validated data

        Args:
            data (dict): Dictionary containing district
                fields
        
        Returns:
            district (District): District object. If no
                data is provided, returns None

        """

        if not data:
            return
        
        district_id = data.pop('id', None)
        district = District.objects.filter(
            tag=data.get('tag'),
            name=data.get('name')
        )
        if district:
            district = district.last()
        else:
            district = District.objects.create(**data)

        return district

    # TODO: There's probably a better way to do this. Need to
    # update relationships and make sure each object uniqueness makes
    # sense.
    def create(self, validated_data):
        """
        Override to create related address and causes

        """

        address_data = validated_data.pop('address', None)
        causes_data = validated_data.pop('causes', [])

        # Create Supporter object        
        supporter = Supporter.objects.create(**validated_data)
        
        # Create Address if info provided
        if address_data is not None:
            district_data = address_data.pop('district', None)
            district = self._get_or_create_district(district_data)
            address_data['district'] = district

            address_id = address_data.pop('id', None)
            address = Address.objects.filter(
                street=address_data.get('street'),
                city=address_data.get('city'),
                zipcode=address_data.get('zipcode'),
                state=address_data.get('state'),
                district_id=district.id if district else None
            ).last()
            if not address:
                address = Address.objects.create(**address_data)
            
            supporter.address = address
            supporter.save(update_fields=['address'])
        
        # Create Cause objects if provided
        for cause in causes_data:
            cause_id = cause.pop('id', None)
            existing_cause = Cause.objects.filter(
                tag=cause.get('tag'), name=cause.get('name')
            )
            if existing_cause:
                cause_obj = existing_cause.last()
            else:
                cause_obj = Cause.objects.create(**cause)
            
            supporter.causes.add(cause_obj)
        
        return supporter
    
    # TODO: There's probably a better way to do this
    def update(self, instance, validated_data):
        """
        Override to update address and causes

        """

        address_data = validated_data.pop('address', None)
        causes_data = validated_data.pop('causes', None)
        super().update(instance, validated_data)

        if address_data is None and causes_data is None:
            return instance
        
        if address_data is not None:
            district_data = address_data.pop('district', None)
            district = self._get_or_create_district(district_data)
            address_data['district'] = district

            address_obj = Address.objects.filter(
                street=address_data.get('street'),
                city=address_data.get('city'),
                zipcode=address_data.get('zipcode'),
                state=address_data.get('state'),
                district_id=district.id if district else None
            )
            if address_obj:
                address_obj = address_obj.last()
                for key, val in address_data.items():
                    setattr(address_obj, key, val)
                address_obj.save()
            else:
                address_obj = Address.objects.create(**address_data)
            
            instance.address = address_obj
            instance.save(update_fields=['address'])
        
        if causes_data is None:
            return instance

        # TODO: Need to change relationship between causes and supporters
        existing_causes = instance.causes.all()
        existing_cause_ids = instance.causes.values_list('id', flat=True)

        created_or_updated_cause_ids = set()
        for cause in causes_data:
            cause_id = cause.pop('id', None)
            cause_obj = Cause.objects.filter(
                tag=cause.get('tag'), name=cause.get('name')
            )
            if cause_obj:
                cause_obj.update(**cause)
                cause_obj = cause_obj.last()
                if cause_obj.id not in existing_cause_ids:
                    instance.causes.add(cause_obj)
            else:
                cause_obj = instance.causes.create(**cause)
                instance.causes.add(cause_obj)

            created_or_updated_cause_ids.add(cause_obj.id)
        
        to_remove_causes_qs = existing_causes.exclude(
            id__in=created_or_updated_cause_ids
        )
        for cause in to_remove_causes_qs:
            instance.causes.remove(cause)
        
        return instance

    class Meta:
        model = Supporter
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phonenumber',
            'address',
            'causes',
        )
