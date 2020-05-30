from rest_framework.generics import *
from rest_framework.response import Response

from myresources.serializer import *


class ClasseView(ListAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_serializer()

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})
