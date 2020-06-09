from rest_framework import serializers

from myresources.models import Teacher
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions', 'is_active']


class AvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar']


class UserUpdatePersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'matricule', 'sexe', 'email']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = []
