from django.test import TestCase
from obb.models import ICE, TrainSection, Person


class ICETestCase(TestCase):
    def setUp(self):
        person = Person.objects.create(first_name='John', last_name='Doe')
        train_section = TrainSection.objects.create(name='Train section 1')
        ice_1 = ICE.objects.create(name='ICE 1')

        ice_1.train_section = train_section
        train_section.person = person

    def test_getter_id(self):
        ice = ICE.objects.get(pk=1)
        self.assertEqual(ice.id, 1)

    def test_getter_name(self):
        ice = ICE.objects.get(pk=1)
        self.assertEqual(ice.name, 'ICE 1')

    def test_getter_train_section(self):
        ice_train_section = ICE.objects.get(pk=1).train_section.all()
        train_section = TrainSection.objects.get(pk=1)
        self.assertEqual(ice_train_section.first(), train_section)

    def test_getter_train_section_id(self):
        ice_train_section = ICE.objects.get(pk=1).train_section.all()
        self.assertEqual(ice_train_section.first().id, 1)

    def test_getter_train_section_name(self):
        ice_train_section = ICE.objects.get(pk=1).train_section.all()
        self.assertEqual(ice_train_section.first().name, 'Train section 1')

    def test_getter_person(self):
        person_in_train = ICE.objects.get(pk=1).train_section.first().person.first()
        person = Person.objects.get(pk=1)
        self.assertEqual(person_in_train, person)

    def test_getter_person_id(self):
        person_in_train = ICE.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.id, 1)

    def test_getter_person_first_name(self):
        person_in_train = ICE.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.first_name, 'John')

    def test_getter_person_last_name(self):
        person_in_train = ICE.objects.get(pk=1).train_section.first().person.first()
        self.assertEqual(person_in_train.last_name, 'Doe')
