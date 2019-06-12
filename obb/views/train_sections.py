from obb.models import TrainSection
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import TrainSectionSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class TrainSectionViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = TrainSection.objects.all()
        serializer = TrainSectionSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a Train section, in Comment type "name <Train_Section_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        train_section = TrainSection(name=data[1])
        train_section.save()

        return Response(train_section)

    def retrieve(self, request, pk=None):
        queryset = TrainSection.objects.all()
        train_section = get_object_or_404(queryset, pk=pk)
        serializer = TrainSectionSerializer(train_section)

        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data.split(' ')
        train_section = TrainSection.objects.get(pk=pk)
        train_section.name = data[1]
        train_section.save()

        return Response(TrainSectionSerializer(train_section).data)
