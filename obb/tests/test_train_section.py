from django.test import TestCase
from obb.models import TrainSection, Person


class TrainSectionTestCase(TestCase):
    def setUp(self):
        person = Person.objects.create(first_name='John', last_name='Doe')
        train_section = TrainSection.objects.create(name='Train section 1')

        train_section.person = person

    def test_getter_id(self):
        train_section = TrainSection.objects.get(pk=1)
        self.assertEqual(train_section.id, 1)

    def test_getter_name(self):
        train_section = TrainSection.objects.get(pk=1)
        self.assertEqual(train_section.name, 'Train section 1')

    def test_getter_person(self):
        person_in_train = TrainSection.objects.get(pk=1).person.first()
        person = Person.objects.get(pk=1)
        self.assertEqual(person_in_train, person)

    def test_getter_person_id(self):
        person_in_train = TrainSection.objects.get(pk=1).person.first()
        self.assertEqual(person_in_train.id, 1)

    def test_getter_person_first_name(self):
        person_in_train = TrainSection.objects.get(pk=1).person.first()
        self.assertEqual(person_in_train.first_name, 'John')

    def test_getter_person_last_name(self):
        person_in_train = TrainSection.objects.get(pk=1).person.first()
        self.assertEqual(person_in_train.last_name, 'Doe')
