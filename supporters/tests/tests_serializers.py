# *****************************************************************************
# supporters/tests/tests.py
# *****************************************************************************

from django.test import TestCase

from supporters.models import Address, Supporter, District, Cause
from supporters.serializers import (
    AddressSerializer, CauseSerializer, DistrictSerializer, SupporterSerializer 
)

# *****************************************************************************
# DistrictSerializerTestCase
# *****************************************************************************


class DistrictSerializerTestCase(TestCase):
    
    """
    A test case for DistrictSerializer

    """

    def setUp(self):
        super().setUp()

        # ***** Create Districts *****
        # Create districts for testing
        self.dist1 = District.objects.create(
            tag='dist1',
            name='District 1'
        )
    
    def tearDown(self):
        super().tearDown()
    
    def test_serializer_should_create_district(self):
        """
        Test that the serializer successfully creates a 
        District object with correct payload

        """

        self.assertEqual(District.objects.count(), 1)

        fake_payload = {
            'tag': 'KY1',
            'name': 'KY District 1'
        }

        serializer = DistrictSerializer(data=fake_payload)
        self.assertTrue(serializer.is_valid())

        # ***** If the serializer is valid, calling save will save the 
        # object to the database *****
        serializer.save()
        self.assertEqual(District.objects.count(), 2)

        district = District.objects.last()
        self.assertEqual(district.tag, 'KY1')
        self.assertEqual(district.tag, 'KY District 1')

    def test_serializer_should_update_district(self):
        """
        Test that the serializer successfully creates a 
        District object with correct payload

        """

        self.assertEqual(District.objects.count(), 1)

        validated_data = {'tag': 'DIS1'}

        serializer = DistrictSerializer()
        serializer.update(self.dist1, validated_data)

        self.assertEqual(District.objects.count(), 1)
        self.dist1.refresh_from_db()

        self.assertEqual(self.dist1.tag, 'DIS1')


# *****************************************************************************
# AddressSerializerTestCase
# *****************************************************************************


class AddressSerializerTestCase(TestCase):
    
    """
    A test case for AddressSerializer

    """

    def setUp(self):
        super().setUp()

        # ***** Create District *****
        self.dist1 = District.objects.create(
            tag='dist1',
            name='District 1'
        )
        
         # ***** Create Address *****
        self.adr1 = Address.objects.create(
            street='Wallaby Way',
            city='Sydney',
            zipcode='02133',
            state='NH',
            district=dist1            
        )
    
    def tearDown(self):
        super().tearDown()
    
    def test_serializer_should_create_address(self):
        """
        Test that the serializer successfully creates an 
        Address object with correct payload

        """

        self.assertEqual(Address.objects.count(), 1)

        fake_payload = {
            'street': '123 Fake St.',
            'city': 'Faketropolis',
            'zipcode': '123456',
            'state': 'NY',
            'district': self.dist1.id
        }

        serializer = AddressSerializer(data=fake_payload)
        self.assertTrue(serializer.is_valid())

        # ***** If the serializer is valid, calling save will save the 
        # object to the database *****
        serializer.save()
        self.assertEqual(Address.objects.count(), 2)

        addr = Address.objects.last()
        self.assertEqual(addr.street, '123 Fake St.')
        self.assertEqual(addr.city, 'Faketropolis')
        self.assertEqual(addr.zipcode, '123456')
        self.assertEqual(addr.state, 'NY')
        self.assertEqual(addr.district.id, self.dist1.id)

    def test_serializer_should_update_address(self):
        """
        Test that the serializer successfully updates a 
        District object with correct payload

        """

        self.assertEqual(District.objects.count(), 1)

        validated_data = {'tag': 'DIS1'}

        serializer = DistrictSerializer()
        serializer.update(self.dist1, validated_data)

        self.assertEqual(District.objects.count(), 1)
        self.dist1.refresh_from_db()

        self.assertEqual(self.dist1.tag, 'DIS1')



# *****************************************************************************
# SupporterSerializerTestCase
# *****************************************************************************


# class SupporterSerializerTestCase(TestCase):
    
#     """
#     A test case for SupportSerializer

#     """

#     def setUp(self):
#         super().setUp()

#         # ***** Create Cause *****
#         cause = Cause.objects.create(
#             tag='caus1',
#             name='Police Brutality',
#             description='Ending police brutality.'
#         )

#         # ***** Create District *****
#         dist = District.objects.create(
#             tag='dist1',
#             name='District 1'
#         )
        
#         # ***** Create Address *****
#         adr = Address.objects.create(
#             street='Wallaby Way',
#             city='Sydney',
#             zipcode='02133',
#             state='NH',
#             district=dist         
#         )

#         # ***** Create Supporter *****
#         sup = Supporter.objects.create(
#             first_name='Bill',
#             last_name='Smith',
#             email='billsmith@gmail.com',
#             phonenumber='5551234567',
#             adddress=adr,
#             causes=cause,

#         )

#         fake_payload = {
#             'first_name': 'Joe',
#             'last_name': 'Doe',
#             'email': 'joe@thedoes.com',
#             'phonenumber': '123456789',
#             'address': adr.id
#         }
    
#     def tearDown(self):
#         super().tearDown()
    
#     def test_serializer_should_create_supporter(self):
        

#     def test_serializer_should_update_supporter(self):
#         pass

# class CauseSerializerTestCase(TestCase):
    
#     """
#     A test case for CauseSerializer

#     """

#     def setUp(self):
#         super().setUp()

#         # ***** Create Causes *****
#         # Create causes for testing
#         cause1 = Cause.objects.create(
#             tag='caus1',
#             name='Police Brutality',
#             description='Ending police brutality.'
#         )
    
#     def tearDown(self):
#         super().tearDown()
    
#     def test_serializer_should_create_cause(self):
        

#     def test_serializer_should_update_cause(self):
#         pass