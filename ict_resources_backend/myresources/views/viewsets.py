from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myresources.serializer import *
from myresources.models import Schedule


class ScheduleViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': request.data})
        else:
            return Response({'status': "Erreur de données", 'errors': serializer.errors})