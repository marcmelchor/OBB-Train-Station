from obb.models import Train, TrainSection, Person
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import TrainSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class TrainViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Train.objects.all()
        serializer = TrainSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a Train, in Comment type "" (USE QUOTES)
    def create(self, request):
        train = Train()
        train.save()

        train_section_1 = TrainSection(name='First Section')
        train_section_1.save()
        train_section_2 = TrainSection(name='Second Section')
        train_section_2.save()
        train_section_3 = TrainSection(name='Third Section')
        train_section_3.save()

        train.dock_section(train_section_1)
        train.dock_section(train_section_2)
        train.dock_section(train_section_3)

        person_1 = Person(first_name='First', last_name='Person')
        person_1.save()
        person_2 = Person(first_name='Second', last_name='Person')
        person_2.save()
        person_3 = Person(first_name='Third', last_name='Person')
        person_3.save()

        train_section_1.get_on_train(person_1)
        train_section_2.get_on_train(person_2)
        train_section_3.get_on_train(person_3)

        return Response(TrainSerializer(train).data)

    def retrieve(self, request, pk=None):
        queryset = Train.objects.all()
        train = get_object_or_404(queryset, pk=pk)
        serializer = TrainSerializer(train)

        return Response(serializer.data)

    # Update Train name, in Comment type "name <Train_name>" (USE QUOTES)
    """def update(self, request, pk=None):
        data = request.data.split(' ')
        train = Train.objects.get(pk=pk)
        train.name = data[1]
        train.save()

        return Response(TrainSerializer(train).data)"""

    @detail_route(methods=['get'], url_path='people')
    def people(self, request, pk=None):
        train = Train.objects.get(pk=pk)
        # train.show_current_passengers()
        people_list = []
        sections = train.train_section.all()
        for section in sections:
            for person in section.person.all():
                print(person.first_name + ' ' + person.last_name)
                people_list.append(person.first_name + ' ' + person.last_name)

        return Response(people_list)
