from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response

from functions.functions import verify_for_notification
from myresources.functions import search_schedule_for_teacher_admin_guest
from myresources.serializer import *
from myresources.models import Schedule

from django.contrib.auth import get_user_model
from myresources.utils import *
import io
from rest_framework.parsers import JSONParser

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
    # on va seulement recuperer ceux dont les réservation ont été validé
    def list(self, request, *args, **kwargs):

        id_level = self.request.GET.get('id_level')
        by_type = self.request.GET.get('by_type')
        id_user = self.request.GET.get('id_user')
        id_type = self.request.GET.get('id_type')
        id_classe = self.request.GET.get('id_classe')

        # verifions si id_type est une reservation , pour   changer le type de requete
        try:
            type_schedule = TypeSchedule.objects.get(type=id_type)
            user = User.objects.get(pk=id_user)

            if type_schedule.type == RESERVATION:

                # seul les prof ou admin peuvent avoir les reservation

                if user.is_teacher or user.is_admin:
                    is_reservation = True
                    data_return = search_schedule_for_teacher_admin_guest(self, is_reservation=is_reservation,
                                                                          by_type=by_type,
                                                                          id_level=id_level, id_classe=id_classe
                                                                          , id_type=id_type, etat=ETAT_ATTENTE)
                else:
                    return Response({"errors": "Vous n'avez pas le droit de voir les reservation"},
                                    status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            # si c'est un cours, cc, td, sauf reservation
            else:
                is_reservation = False
                data_return = search_schedule_for_teacher_admin_guest(self, is_reservation=is_reservation,
                                                                      by_type=by_type,
                                                                      id_level=id_level, id_classe=id_classe
                                                                      , id_type=id_type, etat=ETAT_VALIDE)

            return Response({"data": data_return.data})

        except User.DoesNotExist:
            return Response({'data': 'utilisateur non trouvé '}, status=status.HTTP_404_NOT_FOUND)
        except TypeSchedule.DoesNotExist:
            return Response({'data': "reservation n'existe pas "}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):

        # ser

        serializer = ScheduleSerializer(data=request.data)

        if serializer.is_valid():
            # if request.data['id_equipment']:
            #     CreateSheduleWithIdEquipment(request)

            serializer.save()

            # ~gestion des notifications

            json = JSONRenderer().render(serializer.data)
            stream = io.BytesIO(json)
            data = JSONParser().parse(stream)

            verify_for_notification(data)

            return Response({'data': serializer.data, 'status': status.HTTP_200_OK})
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
