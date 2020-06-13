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

    street = models.CharField(null=True, blank=True, max_length=256)
    city = models.CharField(null=True, blank=True, max_length=256)
    zipcode = models.PositiveIntegerField(null=True, blank=True)
    state = models.CharField(null=True, blank=True, max_length=256)
    district = models.ForeignKey(
        'District', 
        related_name='district', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=False)


# *****************************************************************************
# Cause
# *****************************************************************************


class Cause(models.Model):

    """
    Model for Causes object

    """

    tag = models.CharField(max_length=5, unique=True)
    name = models.CharField(null=False, blank=False, max_length=256)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=False)


# *****************************************************************************
# District
# *****************************************************************************


class District(models.Model):

    """
    Model for District
    
    """

    tag = models.CharField(null=False, blank=False, max_length=5)
    name = models.CharField(null=False, blank=False, max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=False)


# *****************************************************************************
# Supporter
# *****************************************************************************


class Supporter(models.Model):
    
    """
    Model for Supporter object

    """

    is_active = models.BooleanField(default=True)
    first_name = models.CharField(null=True, blank=True, max_length=256)
    last_name = models.CharField(null=True, blank=True, max_length=256)
    email = models.EmailField(null=True, blank=True, max_length=256)
    # TODO: Better way to store phone number and validated
    phonenumber = models.CharField(null=True, blank=True, max_length=15)
    address = models.ForeignKey(
        Address, 
        on_delete=models.CASCADE, 
        related_name='address',
        null=True,
        blank=True
    )
    causes = models.ManyToManyField(
        Cause, 
        blank=True, 
        null=True, 
        related_name='supporters'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=False)
