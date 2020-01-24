# lib imports
from rest_framework import viewsets
from rest_framework.response import Response

# app level imports
from .models import IoTData
from .serializers import IoTDataSerializer


class IoTDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint to fetch iot_data
    """
    permission_classes = []
    queryset = IoTData.objects.all().order_by('-id')
    serializer_class = IoTDataSerializer

    def retrieve(self, request, pk=None):
        queryset = IoTData.objects.filter(box_number=pk).last()
        serializer = IoTDataSerializer(queryset)
        return Response(serializer.data)