from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myresources.serializer import *
from myresources.models import Schedule
from django.contrib.auth.models import User

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            data = User.objects.get(pk=pk)

            serializer = UserSerialiser(data)
            return Response({'data': serializer.data})
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND})
