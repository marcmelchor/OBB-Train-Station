from rest_framework import serializers
from obb.models import Person, Platform, Train, TrainSection, TrainStation, ICE, Railjets


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name')


class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    people = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('people',)


class TrainSectionSerializer(serializers.HyperlinkedModelSerializer):

    person = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = TrainSection
        fields = ('id', 'name', 'order', 'person')


class TrainSerializer(serializers.HyperlinkedModelSerializer):

    train_section = TrainSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = ('id', 'train_section')


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


class ICESerializer(serializers.HyperlinkedModelSerializer):

    # dock_train = TrainSerializer(many=True, read_only=True)
    train_section = TrainSectionSerializer(many=True, read_only=True)

    class Meta:
        model = ICE
        fields = ('id', 'name', 'train_section')


class RailjetsSerializer(serializers.HyperlinkedModelSerializer):

    train_section = TrainSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Railjets
        fields = ('id', 'name', 'train_section')

