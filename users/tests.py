from django.test import TestCase
from django.urls import reverse
import pytest
# Create your tests here.
# Django has a built-in user model and authentication system (see https://docs.djangoproject.com/en/3.2/topics/auth/).  
# It is possible to implement our own custom authentication system, but for this example, we will use Django's.
# We will add a basic integration test to test user login, using a fixture to first create a user to log in. 
# Open the tests.py file in the users directory. It should be empty except for a single import.

# Then add a fixture for creating a test user object in the database:
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

# The django_user_model fixture is a built-in fixture. It acts as a shortcut to accessing the User model for this project.
# See: https://pytest-django.readthedocs.io/en/latest/helpers.html#django-user-model
# This fixture creates a new user with the Django create_user() method and sets a username and password.
# Then it returns the username and password as a tuple.  
# Let's write a function to test that logging into the app works, using the test_user fixture as a parameter to first add a user:

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True


# In this code, the client passed in as a parameter is a built-in "dummy web client" provided by Django as part of its testing tools.
# It mimics some of the functionality of a web browser and helps us test interacting with a Django app. 
# For more information, see: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
# Its login() method helps us test that we can log into the app, and the test_user fixture makes sure that we have a valid user to test with.
# Run: pytest -k login -v

