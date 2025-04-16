from django.core.management.base import BaseCommand
from crm.models import AppUser, Address, CustomerRelationship
from faker import Faker
import random
from tqdm import tqdm

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake AppUser, Address, and CustomerRelationship data"

    def handle(self, *args, **kwargs):
        BATCH_SIZE = 10000
        TOTAL = 3000000

        for _ in tqdm(range(0, TOTAL, BATCH_SIZE), desc="Creating records..."):
            addresses = []
            users = []
            relationships = []

            for _ in range(BATCH_SIZE):
                addr = Address(
                    street=fake.street_name(),
                    street_number=fake.building_number(),
                    city_code=fake.postcode(),
                    city=fake.city(),
                    country=fake.country()
                )
                addresses.append(addr)

            Address.objects.bulk_create(addresses)
            address_ids = list(Address.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            for i in range(BATCH_SIZE):
                gender = random.choice(['M', 'F', 'O'])
                user = AppUser(
                    first_name=fake.first_name_male() if gender == 'M' else fake.first_name_female(),
                    last_name=fake.last_name(),
                    gender=gender,
                    customer_id=fake.uuid4(),
                    phone_number=fake.phone_number(),
                    birthday=fake.date_of_birth(minimum_age=18, maximum_age=90),
                    address_id=address_ids[i]
                )
                users.append(user)

            AppUser.objects.bulk_create(users)
            user_ids = list(AppUser.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            for user_id in user_ids:
                rel = CustomerRelationship(
                    appuser_id=user_id,
                    points=random.randint(0, 5000)
                )
                relationships.append(rel)

            CustomerRelationship.objects.bulk_create(relationships)

        self.stdout.write(self.style.SUCCESS("Successfully generated 3 million records."))
