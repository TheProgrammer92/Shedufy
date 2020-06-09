from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from myresources.paginate import CustomPagination
from myresources.serializer import *
from myresources.models import Schedule

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from myresources.utils import *

User = get_user_model()


class ScheduleViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(Schedule.objects.all().filter(is_valid=True))
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def create(self, request, *args, **kwargs):

        # serialisation des data

        serializer = ScheduleSerializer(data=request.data)

        if serializer.is_valid():

            if request.data['id_equipment']:
                CreateSheduleWithIdEquipment(request)

            serializer.save()

            ## on l'insert dans la table reservation
            schedule = Schedule.objects.get(pk=serializer.data['id'])
            teacher = Teacher.objects.get(pk=serializer.data['id_teacher'])
            instance = ReservationSchedule()
            instance.id_schedule = schedule
            instance.id_teacher = teacher
            instance.save()
            return Response({'data': request.data, 'status': status.HTTP_200_OK})
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
        queryset = self.filter_queryset(Schedule.objects.filter(id_classe=pk).filter(is_valid=True))
        serializer = ScheduleSerializer(queryset, many=True)
        return Response({"data": serializer.data})


class EquipmentViewset(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Equipment.objects.filter(number__gte=1))

        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


class ReservationScheduleViewset(viewsets.ModelViewSet):
    serializer_class = ReservationScheduleSerializer
    queryset = ReservationSchedule.objects.all()
    pk = None
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': status.HTTP_200_OK})

    def retrieve(self, request, pk=None, *args, **kwargs):
        self.pk = pk

        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):

        ## on veut recuperer le tableau des reservation valid et invalide
        if self.pk is not None:
            queryset_reservation_valid = ReservationSchedule.objects.all().filter(is_failed=True).filter(
                id_teacher=self.pk)
            queryset_reservation_failed = ReservationSchedule.objects.all().filter(is_failed=False).filter(
                id_teacher=self.pk)
        else:
            queryset_reservation_valid = ReservationSchedule.objects.all().filter(is_failed=True)
            queryset_reservation_failed = ReservationSchedule.objects.all().filter(is_failed=False)

        serializer_valid = self.get_serializer(queryset_reservation_valid, many=True)
        serializer_failed = self.get_serializer(queryset_reservation_failed, many=True)

        tab_reservation_valid = []

        for reservation_valid in serializer_valid.data:
            ##on recupere les emploie de temps
            instance_schedule = Schedule.objects.filter(pk=reservation_valid["id_schedule"])

            serializer_schedule = ScheduleSerializer(instance_schedule, many=True)
            # pour avoir l'id de la reservation et non l'id  du schedule
            serializer_schedule.data[0].update(id_reservation=reservation_valid["id"])
            serializer_schedule.data[0].update(message=reservation_valid["message"])
            # serializer_schedule.data[0].update(links=serializer_valid["links"])
            # serializer_schedule.data[0].update(total=serializer_valid["total"])
            # serializer_schedule.data[0].update(page=serializer_valid["page"])
            # serializer_schedule.data[0].update(page_size=serializer_valid["page_size"])
            # serializer_schedule.data[0].update(page_size=serializer_valid["page_size"])

            tab_reservation_valid.append(serializer_schedule.data[0])

        tab_reservation_failed = []

        # on recupere les classe pour les ajouter

        for reservation_failed in serializer_failed.data:
            ##on recupere les emploie de temps
            instance_schedule = Schedule.objects.filter(pk=reservation_failed["id_schedule"])

            serializer_schedule = ScheduleSerializer(instance_schedule, many=True)
            # pour avoir l'id de la reservation et non l'id  du schedule
            serializer_schedule.data[0].update(id_reservation=reservation_failed["id"])
            serializer_schedule.data[0].update(message=reservation_failed["message"])

            # serializer_schedule.data[0].update(links=serializer_failed["links"])
            # serializer_schedule.data[0].update(total=serializer_failed["total"])
            # serializer_schedule.data[0].update(page=serializer_failed["page"])
            # serializer_schedule.data[0].update(page_size=serializer_failed["page_size"])

            # on recupere les classe pour les ajouter

            tab_reservation_failed.append(serializer_schedule.data[0])
        return Response({'data_valid': tab_reservation_valid, "data_failed": tab_reservation_failed})

        # les reservaiton qui ont échoué

        # on recupere les classe pour les ajouter

    def update(self, request, pk=None, *args, **kwargs):
        instance = ReservationSchedule.objects.get(pk=pk)

        instance.message = request.data['message']
        instance.is_failed = not instance.is_failed
        instance.save()

        # creation du schedule
        instance_schedule = Schedule.objects.get(pk=instance.id_schedule.id)
        instance_schedule.is_valid = not instance_schedule.is_valid
        instance_schedule.save()

        return Response({'status': status.HTTP_200_OK})
