from django.test import TestCase
from obb.models import Platform, Train, ICE, Railjets


class PlatformTestCase(TestCase):

    def setUp(self):
        train = Train.objects.create()
        ice = ICE.objects.create(name='ICE 1')
        railjet = Railjets.objects.create(name='Railjet 1')

        platform_1 = Platform.objects.create(name='Platform 1')
        platform_1.train = train

        platform_2 = Platform.objects.create(name='Platform 2')
        platform_2.train = ice

        platform_3 = Platform.objects.create(name='Platform 3')
        platform_3.train = railjet

    def test_getter_id(self):
        platform_1 = Platform.objects.get(pk=1)
        self.assertEqual(platform_1.id, 1)

    def test_getter_name(self):
        platform_1 = Platform.objects.get(pk=1)
        self.assertEqual(platform_1.name, 'Platform 1')

    def test_getter_train(self):
        platform_1 = Platform.objects.get(pk=1)
        train = Train.objects.get(pk=1)
        self.assertEqual(platform_1.train, train)

    def test_getter_train_id(self):
        platform_1 = Platform.objects.get(pk=1)
        self.assertEqual(platform_1.train.pk, 1)

    def test_getter_ice(self):
        platform_2 = Platform.objects.get(pk=2)
        ice = ICE.objects.get(pk=2)
        self.assertEqual(platform_2.train.ice, ice)

    def test_getter_ice_id(self):
        platform_2 = Platform.objects.get(pk=2)
        self.assertEqual(platform_2.train.pk, 2)

    def test_getter_ice_name(self):
        platform_2 = Platform.objects.get(pk=2)
        self.assertEqual(platform_2.train.ice.name, 'ICE 1')

    def test_getter_railjet(self):
        platform_3 = Platform.objects.get(pk=3)
        railjet = Railjets.objects.get(pk=3)
        self.assertEqual(platform_3.train.railjets, railjet)

    def test_getter_railjet_id(self):
        platform_3 = Platform.objects.get(pk=3)
        self.assertEqual(platform_3.train.pk, 3)

    def test_getter_railjet_name(self):
        platform_3 = Platform.objects.get(pk=3)
        self.assertEqual(platform_3.train.railjets.name, 'Railjet 1')

    # Get the platform through the Railjet name '_train' > '_railjets' > '_name'
    # Single underscore '_' makes reference to other table (model), like a foreign key or a many to many relation
    # Double underscore '__' makes reference to an attribute of another table (model)
    def test_look_up(self):
        platform = Platform.objects.get(_train__railjets___name='Railjet 1')
        self.assertEqual(platform.train.railjets.id, 3)
