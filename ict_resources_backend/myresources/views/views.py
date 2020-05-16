from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, permissions

from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from myresources.models import userProfile
from myresources.permission import IsOwnerProfileOrReadOnly
from myresources.serializer import *
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.authtoken.models import Token
from djoser.serializers import *
from rest_framework import viewsets


# Create your views here.


class UserProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [ IsOwnerProfileOrReadOnly, IsAuthenticated ]


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        refresh_token = request.data[ "refresh_token" ]

        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class MeListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [ AllowAny ]

    def get(self, request, *args, **kwargs):
        queryset = Token.objects.all()
        serializer = TokenSerializer(queryset, many=True)

        return Response(serializer.data)

