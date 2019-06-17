from obb.models import ICE, TrainSection, Person
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import ICESerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class ICEViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ICE.objects.all()
        serializer = ICESerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a ICE Train, in Comment type "name <ICE_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        ice = ICE(name=data[1])
        ice.save()

        train_section_1 = TrainSection(name='First Section')
        train_section_1.save()
        train_section_2 = TrainSection(name='Second Section')
        train_section_2.save()
        train_section_3 = TrainSection(name='Third Section')
        train_section_3.save()

        ice.dock_section(train_section_1)
        ice.dock_section(train_section_2)
        ice.dock_section(train_section_3)

        person_1 = Person(first_name='First', last_name='Person')
        person_1.save()
        person_2 = Person(first_name='Second', last_name='Person')
        person_2.save()
        person_3 = Person(first_name='Third', last_name='Person')
        person_3.save()

        train_section_1.get_on_train(person_1)
        train_section_2.get_on_train(person_2)
        train_section_3.get_on_train(person_3)

        return Response(ICESerializer(ice).data)

    def retrieve(self, request, pk=None):
        queryset = ICE.objects.all()
        ice = get_object_or_404(queryset, pk=pk)
        serializer = ICESerializer(ice)

        return Response(serializer.data)

    # Update ICE Train name, in Comment type "name <ICE_name>" (USE QUOTES)
    def update(self, request, pk=None):
        data = request.data.split(' ')
        ice = ICE.objects.get(pk=pk)
        ice.name = data[1]
        ice.save()

        return Response(ICESerializer(ice).data)

    @detail_route(methods=['get'], url_path='people')
    def people(self, request, pk=None):
        ice = ICE.objects.get(pk=pk)
        people_list = []
        sections = ice.train_section.all()
        for section in sections:
            for person in section.person.all():
                people_list.append({'id': person.id, "first_name": person.first_name, "last_name": person.last_name})

        person_dict = {'person': people_list}

        return Response(person_dict)
