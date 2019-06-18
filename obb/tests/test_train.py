from django.test import TestCase
from obb.models import Train, TrainSection, Person


class TrainTestCase(TestCase):
    def setUp(self):
        train = Train.objects.create()
        train_section = TrainSection.objects.create(name='Train Section 1')
        person = Person.objects.create(first_name='John', last_name='Doe')
        train.train_section = train_section
        train_section.person = person

    def test_getter_id(self):
        train = Train.objects.get(pk=1)
        self.assertEqual(train.pk, 1)

    def test_getter_train_section(self):
        train_section = Train.objects.get(pk=1).train_section.all()
        self.assertEqual(train_section, train_section)

    def test_getter_train_section_id(self):
        train_section = Train.objects.get(pk=1).train_section.all()
        self.assertEqual(train_section.first().id, 1)

    def test_getter_person(self):
        people = Train.objects.get(pk=1).train_section.get(pk=1).person.all()
        person = Person.objects.get(pk=1)
        self.assertEqual(people.first(), person)

    def test_getter_person_id(self):
        people = Train.objects.get(pk=1).train_section.get(pk=1).person.all()
        self.assertEqual(people.first().id, 1)

    def test_getter_person_first_name(self):
        people = Train.objects.get(pk=1).train_section.get(pk=1).person.all()
        self.assertEqual(people.first().first_name, 'John')

    def test_getter_person_last_name(self):
        people = Train.objects.get(pk=1).train_section.get(pk=1).person.all()
        self.assertEqual(people.first().last_name, 'Doe')
