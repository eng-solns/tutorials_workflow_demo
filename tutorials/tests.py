from django.test import TestCase

# Create your tests here.
from django.urls import reverse
import pytest

from tutorials.models import Tutorial


def test_homepage_access():
    url = reverse('home')
    assert url == "/"


# @pytest.mark.django_db
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"


@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# Notice that new_tutorials() has the parameter db.
# This is a built-in fixture provided by pytest-django. 
# Like the marker @pytest.mark.django_db, this fixture is used by other fixture functions to get access to the connected database.

# Following this fixture function, add these test functions:

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()


# This causes the new_tutorial() fixture function to be run first when either of these tests is run.
# The first test, test_search_tutorials(), simply checks that the object created by the fixture exists, by searching for an object with the same title.
# The second test, test_update_tutorial, updates the title of the new_tutorial object, saves the update, and asserts that a tutorial with the updated name exists in the database. 
# Inside this test function's body, new_tutorial refers not to the new_tutorial fixture function, but to the object returned from that fixture function.
# Run all the tests with the command: 
# pytest -v


# Let's try one more integration test with fixtures, to show how multiple fixtures may be used in a test function.
# To the tests.py file, add another fixture function that creates a different Tutorials object:

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# Next, add a test that uses both fixtures as parameters:
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk   #django ORM .pk refers to primary key


# Both the objects returned from the new_tutorial and another_tutorial fixtures are passed in.
# Then, the test asserts that the .pk attributes are not equal to the other.
# The .pk attribute in the Django ORM refers to the primary key of a database object, which is automatically generated when it is created.
# Thus, this is simply asserting that the two objects are not the same as each other. 
# Rerun the tests with pytest -v and all should pass: 