from obb.models.platform import Platform
from django.shortcuts import get_object_or_404
from obb.serializers.serializers import PlatformSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PlatformViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Platform.objects.all()
        serializer = PlatformSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        data = request.data.split(' ')
        platform = Platform(name=data[0])
        platform.save()

        return Response(platform)

    def retrieve(self, request, pk=None):
        queryset = Platform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = PlatformSerializer(platform)

        return Response(serializer.data)

    def update(self, request, pk=None):
        data = request.data.split(' ')
        platform = Platform.objects.get(pk=pk)
        if data[0] == "name":
            platform.name = data[1]
            platform.save()
        elif data[0] == "train":
            platform.train_id = data[1]
            platform.save()

        return Response(PlatformSerializer(platform).data)
