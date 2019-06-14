from obb.models.platform import Platform, Train, ICE, Railjets
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import PlatformSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PlatformViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Platform.objects.all()
        serializer = PlatformSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a Platform, in Comment type "name: <Platform_name> train_id: <Train_id>" (USE QUOTES)
    def create(self, request):
        kwargs = {}
        data = request.data.split(' ')

        if len(data[1]) > 0:
            kwargs.update({'name': data[1]})

        if data[3] > 0 and data[3].is_numeric():
            queryset = Train.objects.all()
            train = get_object_or_404(queryset, pk=data[3])
            if type(train) is Train:
                kwargs.update({'train_id': train.id})

        platform = Platform(**kwargs)
        platform.save()
        serializer = PlatformSerializer(platform)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Platform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = PlatformSerializer(platform)

        return Response(serializer.data)

    # Update a Train station name, in Comment type "name: <Train_Station_name>" or "train: <Train_id>" (USE QUOTES)
    def update(self, request, pk=None):
        data = request.data.split(' ')
        platform = Platform.objects.get(pk=pk)
        if data[0] == "name":
            platform.name = data[1]
            platform.save()
        elif data[0] == "train":
            queryset = Train.objects.all()
            train = get_object_or_404(queryset, pk=data[1])
            if type(train) is Train:
                platform.train_id = data[1]
                platform.save()

        return Response(PlatformSerializer(platform).data)
