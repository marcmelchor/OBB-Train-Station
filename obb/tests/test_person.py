from django.test import TestCase
from obb.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        person = Person.objects.create(first_name='John', last_name='Doe')

    def test_getter_id(self):
        person = Person.objects.get(pk=1)
        self.assertEqual(person.id, 1)

    def test_getter_first_name(self):
        person = Person.objects.get(pk=1)
        self.assertEqual(person.first_name, 'John')

    def test_getter_last_name(self):
        person = Person.objects.get(pk=1)
        self.assertEqual(person.last_name, 'Doe')
