from obb.models import TrainStation
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import TrainStationSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class TrainStationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = TrainStation.objects.all()
        serializer = TrainStationSerializer(queryset, many=True)

        return Response(serializer.data)

    # Create a Train station, in Comment type "name <Train_Station_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        train_station = TrainStation(name=data[1])
        train_station.save()

        return Response(train_station)

    def retrieve(self, request, pk=None):
        queryset = TrainStation.objects.all()
        train_station = get_object_or_404(queryset, pk=pk)
        serializer = TrainStationSerializer(train_station)

        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data.split(' ')
        train_station = TrainStation.objects.get(pk=pk)
        train_station.name = data[1]
        train_station.save()

        return Response(TrainStationSerializer(train_station).data)

