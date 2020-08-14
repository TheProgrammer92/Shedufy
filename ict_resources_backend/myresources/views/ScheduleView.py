from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView

from rest_framework.response import Response

from myresources.serializer import *
from myresources.models import Schedule

from django.contrib.auth import get_user_model
from myresources.utils import *

User = get_user_model()


class TypeScheduleView(ListAPIView):
    serializer_class = TypeScheduleSerializer

    def list(self, request, *args, **kwargs):
        queryset = TypeSchedule.objects.all()

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


class ScheduleViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    # on va afficher en  fonction de la salle,niveau, cours
    def list(self, request, *args, **kwargs):

        id_level = self.request.GET.get('id_level')
        by_type = self.request.GET.get('by_type')
        id_user = self.request.GET.get('id_user')
        id_type = self.request.GET.get('id_type')
        id_classe = self.request.GET.get('id_classe')
        if by_type == "level":
            queryset = self.filter_queryset(
                Schedule.objects.all().filter(id_level=id_level, id_type=id_type))
            serializer = ScheduleSerializer(queryset, many=True)
            return Response({"data": serializer.data})

        if by_type == "salle":
            queryset = self.filter_queryset(
                Schedule.objects.all().filter(id_classe=id_classe, id_type=id_type))
            serializer = ScheduleSerializer(queryset, many=True)
            return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):

        # ser

        serializer = ScheduleSerializer(data=request.data)

        if serializer.is_valid():
            # if request.data['id_equipment']:
            #     CreateSheduleWithIdEquipment(request)

            serializer.save()

            # on recupere le type d'evenement et on ajoute a manytomany

            return Response({'status': status.HTTP_200_OK})
        # else:
        #     return Response({'status': "Erreur de données", 'errors': serializer.errors})

    def destroy(self, request, pk=None, *args):

        try:
            data = Schedule.objects.get(pk=pk)
            data.delete()
            return Response({'status': status.HTTP_204_NO_CONTENT})
        except:
            return Response({'status': status.HTTP_404_NOT_FOUND})

    def update(self, request, pk=None, *args, **kwargs):

        try:
            instance = Schedule.objects.get(pk=pk)
            serializer = self.get_serializer(instance, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': status.HTTP_200_OK})

        except:

            return Response({'status': status.HTTP_404_NOT_FOUND})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.filter_queryset(Schedule.objects.filter(id_classe=pk).filter(is_valid=True))
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})
