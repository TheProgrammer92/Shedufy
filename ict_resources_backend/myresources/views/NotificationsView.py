from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView

from rest_framework.response import Response

from myresources.serializer import *

from django.contrib.auth import get_user_model

User = get_user_model()


class CategorieNotificationView(ListAPIView):
    queryset = CategorieNotifications.objects.all()

    def list(self, request, *args, **kwargs):
        query = CategorieNotifications.objects.all()
        serializer = CategorieNotificationSerializer(query, many=True)

        return Response({"data": serializer.data})


class NotificationsViewset(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        id_user = self.request.GET.get('id_user')

        query = Notifications.objects.filter(id_receiver=id_user).order_by("-pk")
        serializer = NotificationSerializer(query, many=True)
        return Response({"data": serializer.data})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Notifications.objects.filter(pk=pk)
        serializer = NotificationSerializer(queryset, many=True)

        tab_notification = []

        for notification in serializer.data:
            schedule = Schedule.objects.get(pk=notification['id_event'])

            tab = {}

            tab["id_department"] = schedule.id_department.pk
            tab['department_name'] = schedule.id_department.department_name
            tab['id_level'] = schedule.id_level.pk

            tab['id_type'] = schedule.id_type.pk
            tab['type_reservation'] = schedule.type_reservation.pk

            tab.update(notification)

            tab_notification.append(tab)

            # cherchons le partement

        return Response({"data": tab_notification})
