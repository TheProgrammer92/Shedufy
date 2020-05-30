from rest_framework import serializers

from myresources.models import *


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenModel
        exclude = []


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['name', 'start', 'end', 'details', 'color', 'id', 'id_classe','id_equipment']


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions', 'is_active']


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['code_classe', 'id']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['equipment', 'id', 'number']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationEquipment
        fields = ['id_equipment', 'number']
