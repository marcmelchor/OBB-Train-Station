from obb.models.person import Person
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PersonViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a Person, in Comment type "<Person_first_name> <Person_last_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        person = Person(first_name=data[0], last_name=data[1])
        person.save()

        return Response(person)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.all()
        person = get_object_or_404(queryset, pk=pk)
        serializer = PersonSerializer(person)

        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data.split(' ')
        person = Person.objects.get(pk=pk)
        if data[0] == "first_name":
            person.first_name = data[1]
            person.save()
        elif data[0] == "last_name":
            person.last_name = data[1]
            person.save()

        return Response(PersonSerializer(person).data)
