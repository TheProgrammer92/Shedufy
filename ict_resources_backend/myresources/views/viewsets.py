from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from myresources.serializer import *
from myresources.models import Schedule

from django.core.exceptions import ObjectDoesNotExist


class ScheduleViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        id_equip = request.data['id_equipment']
        if serializer.is_valid():
            instance = Equipment.objects.get(pk=id_equip)

            if instance.number != 0:
                number_instance = instance.number
                instance.number -= 1
                instance.save()

                # verication si il es dans reservation table , sinon , on le modifie

                try:

                    instance_reservation = ReservationEquipment.objects.get(id_equipment=id_equip)
                    datas = {'id_equipment': id_equip, 'number': (instance_reservation.number + 1)}

                    serializer_reservation = ReservationSerializer(instance_reservation, data=datas)
                    if serializer_reservation.is_valid(raise_exception=True):
                        serializer_reservation.save()

                except ReservationEquipment.DoesNotExist:

                    datas = {'id_equipment': id_equip, 'number': 1}

                    serializer_reservation = ReservationSerializer(data=datas)
                    if serializer_reservation.is_valid(raise_exception=True):
                        serializer_reservation.save()

            serializer.save()
            return Response({'data': request.data})
        else:
            return Response({'status': "Erreur de données", 'errors': serializer.errors})

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
        queryset = self.filter_queryset(Schedule.objects.filter(id_classe=pk))
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})


class ClasseViewset(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


class EquipmentViewset(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Equipment.objects.filter(number__gte=1))

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})
