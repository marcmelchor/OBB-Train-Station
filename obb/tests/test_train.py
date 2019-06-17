from django.test import TestCase
from obb.models import Train, TrainSection


class TrainTestCase(TestCase):
    def setUp(self):
        train = Train.objects.create()
        train_section = TrainSection.objects.create(name='Train Section 1')
        train.train_section = train_section

    def test_getter_id(self):
        train = Train.objects.get(pk=1)
        self.assertEqual(train.pk, 1)

    def test_getter_train_section_id(self):
        train = Train.objects.get(pk=1)
        self.assertEqual(train.train_section.first.pk, 1)

