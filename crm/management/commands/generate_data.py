from django.core.management.base import BaseCommand
from crm.models import (
    AppUser, Address, CustomerRelationship,
    OptimizedAppUser, OptimizedAddress, OptimizedCustomerRelationship
)
from faker import Faker
import random
from tqdm import tqdm

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake AppUser, Address, and CustomerRelationship data and copy to optimized models"

    def handle(self, *args, **kwargs):
        BATCH_SIZE = 10000
        TOTAL = 3000000

        for _ in tqdm(range(0, TOTAL, BATCH_SIZE), desc="Creating records..."):
            # Step 1: Create unoptimized Address
            addresses = [Address(
                street=fake.street_name(),
                street_number=fake.building_number(),
                city_code=fake.postcode(),
                city=fake.city(),
                country=fake.country()
            ) for _ in range(BATCH_SIZE)]
            Address.objects.bulk_create(addresses)

            address_ids = list(Address.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            # Step 2: Create AppUser
            users = []
            for i in range(BATCH_SIZE):
                gender = random.choice(['M', 'F', 'O'])
                users.append(AppUser(
                    first_name=fake.first_name_male() if gender == 'M' else fake.first_name_female(),
                    last_name=fake.last_name(),
                    gender=gender,
                    customer_id=fake.uuid4(),
                    phone_number=fake.phone_number(),
                    birthday=fake.date_of_birth(minimum_age=18, maximum_age=90),
                    address_id=address_ids[i]
                ))
            AppUser.objects.bulk_create(users)

            user_ids = list(AppUser.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            # Step 3: Create CustomerRelationship
            relationships = [CustomerRelationship(
                appuser_id=user_ids[i],
                points=random.randint(0, 5000)
            ) for i in range(BATCH_SIZE)]
            CustomerRelationship.objects.bulk_create(relationships)

            # Step 4: Copy to OptimizedAddress
            OptimizedAddress.objects.bulk_create([
                OptimizedAddress(**{
                    field.name: getattr(addr, field.name)
                    for field in OptimizedAddress._meta.fields
                    if field.name != 'id'
                }) for addr in addresses
            ])
            optimized_address_ids = list(OptimizedAddress.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            # Step 5: Copy to OptimizedAppUser
            OptimizedAppUser.objects.bulk_create([
                OptimizedAppUser(**{
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'gender': user.gender,
                    'customer_id': user.customer_id,
                    'phone_number': user.phone_number,
                    'birthday': user.birthday,
                    'address_id': optimized_address_ids[i]
                }) for i, user in enumerate(users)
            ])
            optimized_user_ids = list(OptimizedAppUser.objects.order_by('-id')[:BATCH_SIZE].values_list('id', flat=True))

            # Step 6: Copy to OptimizedCustomerRelationship
            OptimizedCustomerRelationship.objects.bulk_create([
                OptimizedCustomerRelationship(
                    appuser_id=optimized_user_ids[i],
                    points=relationships[i].points
                ) for i in range(BATCH_SIZE)
            ])

        self.stdout.write(self.style.SUCCESS("Successfully generated and cloned 3 million records."))
