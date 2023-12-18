import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lvl2assessment.settings')  # Replace with your actual Django project settings module

# Initialize Django
django.setup()

# Import your models after Django setup
from lvl2app.models import USERS


def resetServer():
    user_input = input("Are you sure you want to delete all the data? (y/n): ").lower()

    if user_input == 'y':
        print("You entered 'y'. Deleting data....")
        print(USERS.objects.all())
        users_to_delete = USERS.objects.all()
        users_to_delete.delete()
        users = USERS.objects.all()
        print("Data deleted....")

    elif user_input == 'n':
        print("You entered 'n'. Aborting the action.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        resetServer()


if __name__ == '__main__':
   
    resetServer()
    