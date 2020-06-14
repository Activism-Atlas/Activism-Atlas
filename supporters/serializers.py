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

    def _get_and_create_district(self, data):
        """
        Helper method to create District object from
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
        
        district, _ = District.objects.get_or_create(**data)
        return district

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
            district = self._get_and_create_district(district_data)
            address_data['district'] = district

            address = Address.objects.create(**address_data)
            supporter.address = address
            supporter.save(update_fields=['address'])
        
        # Create Cause objects if provided
        for cause in causes_data:
            supporter.causes.add(**cause)
        
        return supporter

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
