# lib imports
import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

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
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)

    def list(self, request, *args, **kwargs):
        serializer = IoTDataSerializer(self.queryset, many=True)

        if request.accepted_renderer.format == 'html':
            return render(
                request,
                'list.html',
                {"data": serializer.data},
            )
        return Response(serializer.data)
