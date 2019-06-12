from rest_framework import serializers
from obb.models import Person, Platform, Train, TrainSection, TrainStation, ICE, Railjets


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')


class TrainSectionSerializer(serializers.HyperlinkedModelSerializer):

    person = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = TrainSection
        fields = ('name', 'order', 'person')


class TrainSerializer(serializers.HyperlinkedModelSerializer):

    train_section = TrainSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = ('id', 'train_section')


class ICESerializer(serializers.HyperlinkedModelSerializer):

    dock_train = TrainSerializer(many=True, read_only=True)

    class Meta:
        model = ICE
        fields = ('id', 'name', 'dock_train')


class RailjetsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Railjets
        fields = ('id', 'name')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    train = TrainSerializer(read_only=True)

    class Meta:
        model = Platform
        fields = ('id', 'name', 'train')


class TrainStationSerializer(serializers.HyperlinkedModelSerializer):

    platform = PlatformSerializer(many=True, read_only=True)

    class Meta:
        model = TrainStation
        fields = ('id', 'name', 'platform')
