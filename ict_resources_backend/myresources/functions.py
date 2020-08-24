from rest_framework.response import Response

from myresources.models import Schedule
from myresources.serializer import ScheduleSerializer
from myresources_profil.constants import TEACHER_TYPE


def load_schedule_for_teacher_admin(by_type, is_reservation, id_level, id_type, etat, id_classe):
    if by_type == "level":
        if is_reservation:
            return Schedule.objects.all().filter(id_level=id_level, type_reservation=id_type)
        if not is_reservation:
            return Schedule.objects.all().filter(id_level=id_level, id_type=id_type, id_etat=etat)

    elif by_type == "salle":
        if is_reservation:
            return Schedule.objects.all().filter(id_classe=id_classe, type_reservation=id_type)
        if not is_reservation:
            return Schedule.objects.all().filter(id_classe=id_classe, id_type=id_type, id_etat=etat)


def load_schedule_for_teacher(id_teacher):
    return Schedule.objects.all().filter(id_teacher=id_teacher)


def search_schedule_for_teacher_admin_guest(self, is_reservation=None, by_type=None, id_level=None, id_classe=None,
                                            id_type=None, etat=None, id_teacher=None):

    if id_type == TEACHER_TYPE:

        queryset = load_schedule_for_teacher(id_teacher)

        serializer = ScheduleSerializer(queryset, many=True)
        return serializer
    else:
        queryset = self.filter_queryset(
            load_schedule_for_teacher_admin(by_type=by_type, is_reservation=is_reservation, id_level=id_level,
                                            id_type=id_type, etat=etat, id_classe=id_classe))
        serializer = ScheduleSerializer(queryset, many=True)
        return serializer
