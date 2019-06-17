from django.test import TestCase
from obb.models import TrainStation, Platform


class TrainStationTestCase(TestCase):
    def setUp(self):
        platform = Platform.objects.create(name='Platform 1')
        TrainStation.objects.create(name='Linz')
        TrainStation.platform = platform

    def test_getter_id(self):
        linz = TrainStation.objects.get(pk=1)
        self.assertEqual(linz.id, 1)

    def test_getter_name(self):
        linz = TrainStation.objects.get(pk=1)
        self.assertEqual(linz.name, 'Linz')

    def test_getter_platform(self):
        linz = TrainStation.objects.get(pk=1)
        platform_1 = Platform.objects.get(pk=1)
        self.assertEqual(linz.platform, platform_1)

    def test_getter_platform_id(self):
        linz = TrainStation.objects.get(pk=1)
        self.assertEqual(linz.platform.pk, 1)

    def test_getter_platform_name(self):
        linz = TrainStation.objects.get(pk=1)
        self.assertEqual(linz.platform.name, 'Platform 1')
