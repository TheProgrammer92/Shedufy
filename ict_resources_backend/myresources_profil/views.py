from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


from rest_framework import status, permissions

from rest_framework.generics import *
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from djoser.serializers import *

from myresources_profil.serializer import *
from myresources_profil.models import *

from functions.functions import *
from .constants import *

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
        serializer = self.get_serializer(queryset, many=True)

        return Response({'data': serializer.data})


# Création d'un étudiant
class CreateUserView(CreateAPIView):
    serializer_class = UserSerialiserCreate
    permission_classes = [AllowAny]

    ##toute personne qui passe ici est un étudiant
    # l'envoie de l'email s'est personalisé dans la method save , du model CustomUser
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = User.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()

        begin_url = CODE_STUDENT
        url = generate_url(request.data['email'], begin_url)
        send_activate_account_mail(request.data['email'], url)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# verification du code
class VerifyCodeView(RetrieveAPIView):
    serializer_class = CodeValidation

    def get(self, request, code, *args, **kwargs):

        try:
            url_to_verify = URL_VALIDATE_CREATE + code
            url = CodeValidation.objects.get(url_code=url_to_verify)

            # si l'url est valide, on supprime l'url et on redirige http l'user
            if url.is_valid:
                url.delete()
                return HttpResponseRedirect(redirect_to=URL_GO_TO_LOGIN)
            # on valide le users
            user = User.objects.get(id=url.id_creator_id)
            user.is_active = True

            ## on supprime l'url
            url.delete()
            user.save(force_update=True, update_fields=['is_active'])
            # put active user
            return Response({"data": "compte a été validé veuiller aller vous connecter "}, status=status.HTTP_200_OK)

        except (CodeValidation.DoesNotExist, User.DoesNotExist) as e:
            return Response({"data": "Cette url n'est pas disponible"}, status=status.HTTP_404_NOT_FOUND)
