# *****************************************************************************
# supporters/models.py
# *****************************************************************************

from django.db import models

# *****************************************************************************
# Address
# *****************************************************************************

class Address(models.Model):

    """
    Model for addresses

    """

    street = models.CharField(blank=False, max_length=256)
    city = models.CharField(blank=True, max_length=256)
    zipcode = models.IntegerField(blank=False, max_length=5)
    state = models.CharField(blank=True, max_length=256)
    district = models.ForeignKey('District', related_name='district')


# *****************************************************************************
# Cause
# *****************************************************************************


class Cause(models.Model):

    """
    Model for Causes object

    """

    tag = models.CharField(blank=False, max_length=5)
    name = models.CharField(blank=False, max_length=256)
    description = models.TextField(blank=True)


# *****************************************************************************
# District
# *****************************************************************************


class District(models.Model):

    """
    Model for District
    
    """

    tag = models.CharField(blank=False, max_length=5)
    name = models.CharField(blank=False, max_length=256)


# *****************************************************************************
# Supporter
# *****************************************************************************


class Supporter(models.Model):
    
    """
    Model for Supporter object

    """

    is_active = models.BooleanField(default=True)
    first_name = models.CharField(blank=True, max_length=256)
    last_name = models.CharField(blank=True, max_length=256)
    email = models.EmailField(blank=True, max_length=256)
    # TODO: Better way to store phone number and validated
    phonenumber = models.CharField(blank=True, max_length=15)
    address = models.ForeignKey(
        Address, 
        on_delete=models.CASCADE, 
        related_name='address'
    )
    district = models.ForeignKey(District, related_name='district')
    causes = models.ForeignKey('SupporterCause', related_name='causes')


# *****************************************************************************
# SupporterCause
# *****************************************************************************


class SupporterCause(models.Model):

    """
    Model for SupporterCause object

    """

    supporter = models.ForeignKey(Supporter, related_name='supporter')
    cause = models.ForeignKey(Cause, related_name='cause')

