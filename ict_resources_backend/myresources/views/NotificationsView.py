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
        query = Notifications.objects.all()
        serializer = NotificationSerializer(query, many=True)
        return Response({"notif": serializer.data})

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Notifications.objects.filter(id_receiver=pk)
        serializer = NotificationSerializer(queryset, many=True)
        return Response({"data": serializer.data})
