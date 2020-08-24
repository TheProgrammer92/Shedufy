from rest_framework import serializers

from myresources.models import *
from django.contrib.auth import get_user_model

from myresources_profil.models import CodeValidation

User = get_user_model()


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []


class UserSerialiserCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']


class AvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']


class UserUpdatePersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'matricule', 'sexe', 'email']


class CodeValidationVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeValidation
        exclude = []
