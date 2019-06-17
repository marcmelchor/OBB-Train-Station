from django.test import TestCase
from obb.models import TrainStation, Platform


class TrainStationTestCase(TestCase):
    def setUp(self):
        platform = Platform.objects.create(name='Platform 1')
        TrainStation.objects.create(name='Linz', platform=platform)

    def test_getters(self):
        linz = TrainStation.objects.get(_name='Linz')
        self.assertEqual(linz.name, 'Linz')
        self.assertEqual(linz.id, 1)
