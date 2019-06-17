from obb.models import Railjets, TrainSection, Person
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import RailjetsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class RailjetsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Railjets.objects.all()
        serializer = RailjetsSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a ICE Train, in Comment type "name <ICE_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        railjet = Railjets(name=data[1])
        railjet.save()

        train_section_1 = TrainSection(name='First Section')
        train_section_1.save()
        train_section_2 = TrainSection(name='Second Section')
        train_section_2.save()
        train_section_3 = TrainSection(name='Third Section')
        train_section_3.save()

        railjet.dock_section(train_section_1)
        railjet.dock_section(train_section_2)
        railjet.dock_section(train_section_3)

        person_1 = Person(first_name='First', last_name='Person')
        person_1.save()
        person_2 = Person(first_name='Second', last_name='Person')
        person_2.save()
        person_3 = Person(first_name='Third', last_name='Person')
        person_3.save()

        train_section_1.get_on_train(person_1)
        train_section_2.get_on_train(person_2)
        train_section_3.get_on_train(person_3)

        return Response(RailjetsSerializer(railjet).data)

    def retrieve(self, request, pk=None):
        queryset = Railjets.objects.all()
        railjet = get_object_or_404(queryset, pk=pk)
        serializer = RailjetsSerializer(railjet)

        return Response(serializer.data)

    # Update Railjet Train name, in Comment type "name <ICE_name>" (USE QUOTES)
    def update(self, request, pk=None):
        data = request.data.split(' ')
        railjet = Railjets.objects.get(pk=pk)
        railjet.name = data[1]
        railjet.save()

        return Response(RailjetsSerializer(railjet).data)

    @detail_route(methods=['get'], url_path='people')
    def people(self, request, pk=None):
        railjet = Railjets.objects.get(pk=pk)
        people_list = []
        sections = railjet.train_section.all()
        for section in sections:
            for person in section.person.all():
                people_list.append({'id': person.id, "first_name": person.first_name, "last_name": person.last_name})

        person_dict = {'person': people_list}

        return Response(person_dict)
