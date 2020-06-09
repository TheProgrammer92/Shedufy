from django.shortcuts import render

# Create your views here.


from rest_framework import status, permissions

from rest_framework.generics import *
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from PIL import Image

from rest_framework.authtoken.models import Token
from djoser.serializers import *

from myresources_profil.serializer import *
from django.contrib.auth import get_user_model

User = get_user_model()


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        refresh_token = request.data["refresh_token"]

        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class MeListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [AllowAny]
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        queryset = Token.objects.all()
        serializer = TokenSerializer(queryset, many=True)

        return Response(serializer.data)


class UserUpdatePersonnalInfoView(UpdateAPIView):
    serializer_class = UserUpdatePersonalInfoSerializer

    def update(self, request, *args, **kwargs):

        try:
            instance = User.objects.filter(pk=request.data['id'])
            serializer = self.get_serializer(instance, data=request.data)

            if serializer.is_valid(raise_exception=False):
                serializer.save()
                return Response({'status': status.HTTP_200_OK})

        except:

            return Response({'status': status.HTTP_404_NOT_FOUND})


class AvatarUpdateView(UpdateAPIView):
    parser_classes = [FileUploadParser]

    def update(self, request, *args, **kwargs):
        file = request.data['avatar']

        User.avatar.save(file.name, file, save=True)

        return Response({'status': status.HTTP_404_NOT_FOUND})


class GetAllUser(ListAPIView):
    serializer_class = UserSerialiser
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)

        return Response({'data': serializer.data})
