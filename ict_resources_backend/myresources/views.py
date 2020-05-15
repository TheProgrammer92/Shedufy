from django.shortcuts import render

from rest_framework import status, permissions

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import userProfile
from .permission import IsOwnerProfileOrReadOnly
from .serializer import userProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken


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
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class LogoutAndBlacklistRefreshTokenForUserView(APIView):


    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):

            refresh_token = request.data["refresh_token"]

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
