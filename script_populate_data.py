# *****************************************************************************
# Activism-Atlas/script_populate_data.py
# *****************************************************************************

import re

from faker import Factory
from random import randint, sample

from supporters.models import (
    Address,
    Cause,
    District,
    Supporter
)

fake = Factory.create('en_US')

CAUSES = [
    {'tag': 'HAL', 'name': 'Half by 2030'},
    {'tag': 'REF', 'name': 'Police Reform'},
    {'tag': 'GER', 'name': 'Gerrymandering'},
    {'tag': 'RIK', 'name': 'Close Rikers'},
]
MAX_CAUSES = len(CAUSES)
NUM_OF_ACTIVE_SUPPORTERS = 100
NUM_OF_INACTIVE_SUPPORTERS = 20

# *****************************************************************************
# create_districts
# *****************************************************************************


def create_district():
    random_district_num = randint(1, 50)

    tag = 'D' + str(random_district_num)
    name = 'District ' + str(random_district_num)

    district, _ = District.objects.get_or_create(
        tag=tag,
        name=name,
    )

    return district
    

# *****************************************************************************
# create_address
# *****************************************************************************


def create_address():

    is_ny = False
    while not is_ny:
        fake_addr = fake.address()
        try:
            street, city_state_zip = fake_addr.split('\n')
            city, state_zip = city_state_zip.split(', ')
            state, zipcode = state_zip.split(' ')
        except ValueError:
            continue

        if state == 'NY':
            is_ny = True

    
    district = create_district()

    address = Address.objects.create(
        street=street,
        city=city,
        zipcode=zipcode,
        state=state,
        district=district
    )

    return address


# *****************************************************************************
# generate_fake_supporter_info
# *****************************************************************************


def generate_fake_supporter_info():

    phonenumber = fake.phone_number()
    
    # Remove extension and chars
    phonenumber = phonenumber.split('x')[0]
    phonenumber = re.sub('[^0-9]', '',phonenumber)
    if len(phonenumber) > 15:
        phonenumber = phonenumber[:15]

    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'phonenumber': phonenumber
    }

# *****************************************************************************
# Generate Data
# *****************************************************************************

# ***** Create Causes *****
cause_ids = set()
for c in CAUSES:
    cause, _ = Cause.objects.get_or_create(**c)
    cause_ids.add(cause.id)


# ***** Create Supporters and Related *****
for i in range(1, NUM_OF_ACTIVE_SUPPORTERS+1):
    
    address = create_address()

    supporter_data = generate_fake_supporter_info()
    supporter_data['address'] = address

    created = False
    while not created:
        supporter, created = Supporter.objects.get_or_create(
            **supporter_data
        )

    # Get a random number of causes that the supporter supports
    num_causes = randint(1, MAX_CAUSES)

    # Get a list of random cause IDs to get and add to supporter
    cause_ids_to_get = sample(cause_ids, num_causes)
    for id in cause_ids_to_get:
        cause = Cause.objects.get(id=id)
        supporter.causes.add(cause)
        