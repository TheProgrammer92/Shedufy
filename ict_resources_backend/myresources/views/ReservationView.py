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


class ReservationViewset(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    # on va afficher en  fonction de la salle,niveau, cours
    # on va seulement recuperer ceux dont les réservation ont été validé
    def list(self, request, *args, **kwargs):
        # reservation Valide
        queryset_valid = self.filter_queryset(Schedule.objects.all().filter(id_etat=ETAT_VALIDE))
        serializer_valid = ScheduleSerializer(queryset_valid, many=True)

        # en attente
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_etat=ETAT_ATTENTE))
        serializer_attente = ScheduleSerializer(queryset, many=True)

        # etat annullé
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_etat=ETAT_ANNULLE))
        serializer_annulle = ScheduleSerializer(queryset, many=True)

        # état refusé
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_etat=ETAT_REFUS))
        serializer_refus = ScheduleSerializer(queryset, many=True)

        return Response({
            "reservation_valid": serializer_valid.data,
            "reservation_attente": serializer_attente.data,
            "reservation_annulle": serializer_annulle.data,
            "reservation_refus": serializer_refus.data,

        })

    def retrieve(self, request, pk=None, *args, **kwargs):
        # TODO: verifier si c'est un utilisateur ici si c'est un professeur, pour avoir les reservation

        id_user = pk

        # reservation Valide
        queryset_valid = self.filter_queryset(Schedule.objects.all().filter(id_user=id_user, id_etat=ETAT_VALIDE))
        serializer_valid = ScheduleSerializer(queryset_valid, many=True)

        # en attente
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_user=id_user, id_etat=ETAT_ATTENTE))
        serializer_attente = ScheduleSerializer(queryset, many=True)

        # etat annullé
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_user=id_user, id_etat=ETAT_ANNULLE))
        serializer_annulle = ScheduleSerializer(queryset, many=True)

        # état refusé
        queryset = self.filter_queryset(Schedule.objects.all().filter(id_user=id_user, id_etat=ETAT_REFUS))
        serializer_refus = ScheduleSerializer(queryset, many=True)

        return Response({
            "reservation_valid": serializer_valid.data,
            "reservation_attente": serializer_attente.data,
            "reservation_annulle": serializer_annulle.data,
            "reservation_refus": serializer_refus.data,

        })
