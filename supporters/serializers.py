# *****************************************************************************
# supporters/serializers.py
# *****************************************************************************

from rest_framework import serializers

from . import models

# *****************************************************************************
# DistrictSerializer
# *****************************************************************************


class DistrictSerializer(serializers.ModelSerializer):
    
    """
    A serializer to serializer District objects.

    """

    class Meta:
        model = models.District
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

    district = DistrictSerializer(required=False)

    class Meta:
        model = models.Address
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

    class Meta:
        model = models.Cause
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

    address = AddressSerializer(required=False)
    causes = CauseSerializer(required=False, many=True)

    class Meta:
        model = models.Supporter
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phonenumber',
            'address',
            'causes',
        )

    #Add create for nested serializer 
    def create(self, validated_data):
        causes_data = validated_data.pop('causes')
        address_data = validated_data.pop('address')
        supporter = models.Supporter.objects.create(**validated_data)
        #need to create a district instance also to add to the address
        supporter.address = models.Address.objects.create(**address_data)
        # supporter.address.add(**address_data)
        for cause_data in causes_data:
            supporter.causes.add(**cause_data)
        return supporter