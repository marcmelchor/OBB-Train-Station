from obb.models import TrainStation
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import TrainStationSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class TrainStationViewSet(viewsets.ViewSet):

    def list(self, request):
        train_stations = TrainStation.objects.all()
        serializer = TrainStationSerializer(train_stations, many=True)

        return Response(serializer.data)

    # Create a Train station, in Comment type "name: <Train_Station_name>" (USE QUOTES)
    def create(self, request):
        data = request.data.split(' ')
        train_station = TrainStation(name=data[1])
        train_station.save()
        serializer = TrainStationSerializer(train_station)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TrainStation.objects.all()
        train_station = get_object_or_404(queryset, pk=pk)
        serializer = TrainStationSerializer(train_station)

        return Response(serializer.data)

    # Update a Train station name, in Comment type "name: <Train_Station_name>" (USE QUOTES)
    def update(self, request, pk=None):
        data = request.data.split(' ')
        queryset = TrainStation.objects.all()
        train_station = get_object_or_404(queryset, pk=pk)
        train_station.name = data[1]
        train_station.save()
        serializer = TrainStationSerializer(train_station)

        return Response(serializer.data)
