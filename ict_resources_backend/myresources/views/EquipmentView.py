from rest_framework import status, viewsets

from rest_framework.response import Response


from myresources.serializer import *

from django.contrib.auth import get_user_model
from myresources.utils import *

User = get_user_model()


class EquipmentViewset(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Equipment.objects.filter(number__gte=1))

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})