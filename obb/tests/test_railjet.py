from django.test import TestCase
from obb.models import Railjets, TrainSection, Person


class RailjetTestCase(TestCase):
    def setUp(self):
        person = Person.objects.create(first_name='John', last_name='Doe')
        train_section = TrainSection.objects.create(name='Train section 1')
        railjet = Railjets.objects.create(name='Railjet 1')

        railjet.train_section = train_section
        train_section.person = person

    def test_getter_id(self):
        railjet = Railjets.objects.get(pk=1)
        self.assertEqual(railjet.id, 1)

    def test_getter_name(self):
        railjet = Railjets.objects.get(pk=1)
        self.assertEqual(railjet.name, 'Railjet 1')

    def test_getter_train_section(self):
        railjet_train_section = Railjets.objects.get(pk=1).train_section.all()
        train_section = TrainSection.objects.get(pk=1)
        self.assertEqual(railjet_train_section.first(), train_section)

    def test_getter_train_section_id(self):
        railjet_train_section = Railjets.objects.get(pk=1).train_section.all()
        self.assertEqual(railjet_train_section.first().id, 1)

    def test_getter_train_section_name(self):
        railjet_train_section = Railjets.objects.get(pk=1).train_section.all()
        self.assertEqual(railjet_train_section.first().name, 'Train section 1')

    def test_getter_person(self):
        person_in_train = Railjets.objects.get(pk=1).train_section.first().person.first()
        person = Person.objects.get(pk=1)
        self.assertEqual(person_in_train, person)

    def test_getter_person_id(self):
        person_in_train = Railjets.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.id, 1)

    def test_getter_person_first_name(self):
        person_in_train = Railjets.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.first_name, 'John')

    def test_getter_person_last_name(self):
        person_in_train = Railjets.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.last_name, 'Doe')
