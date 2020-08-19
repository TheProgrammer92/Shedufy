from rest_framework.response import Response

from myresources.models import Schedule
from myresources.serializer import ScheduleSerializer


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
            return Schedule.objects.all().filter(id_classe=id_classe, type_reservation=id_type, id_etat=etat)


def search_schedule_for_teacher_admin_guest(self, is_reservation, by_type, id_level, id_classe, id_type, etat):
    queryset = self.filter_queryset(
            load_schedule_for_teacher_admin(by_type=by_type, is_reservation=is_reservation, id_level=id_level,
                                            id_type=id_type, etat=etat , id_classe=id_classe))
    serializer = ScheduleSerializer(queryset, many=True)
    return serializer


