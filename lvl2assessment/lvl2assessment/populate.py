import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lvl2assessment.settings')  # Replace with your actual Django project settings module

# Initialize Django
django.setup()

# Import your models after Django setup
from lvl2app.models import USERS
from faker import Faker
from random import randrange


fake = Faker()
def populate_db(N=5):

    for i in range(N):
        Faker.seed(randrange(100))
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.free_email()
        users = USERS.objects.get_or_create(first_name = first_name, last_name=last_name, email=email)[0]
        print(users)
        users.save()

if __name__ == '__main__':
    print("Populating Script")
    populate_db(10)
    print("Populating complete!")