# *****************************************************************************
# supporters/tests/tests.py
# *****************************************************************************

from django.test import TestCase

from supporters.models import Address, Supporter, District, Cause
from supporters.serializers import DistrictSerializer

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



# # *****************************************************************************
# # AddressSerializerTestCase
# # *****************************************************************************


# class AddressSerializerTestCase(TestCase):
    
#     """
#     A test case for AddressSerializer

#     """

#     def setUp(self):
#         super().setUp()

#         # ***** Create District *****
#         dist1 = District.objects.create(
#             tag='dist1',
#             name='District 1'
#         )
        
#          # ***** Create Address *****
#         adr1 = Address.objects.create(
#             street='Wallaby Way',
#             city='Sydney',
#             zipcode='02133',
#             state='NH',
#             district=dist1            
#         )
    
#     def tearDown(self):
#         super().tearDown()
    
#     def test_serializer_should_create_address(self):
        

#     def test_serializer_should_update_address(self):
#         pass


class DistrictSerializerTestCase(TestCase):
    
    """
    A test case for DistrictSerializer

    """

    def setUp(self):
        super().setUp()

        # ***** Create Districts *****
        # Create districts for testing
        dist1 = District.objects.create(
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
        fake_payload = {
            ''
        }

    def test_serializer_should_update_district(self):
        pass


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