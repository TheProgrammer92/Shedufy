from rest_framework import serializers

from myresources.models import *


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = userProfile
        fields = '__all__'


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenModel
        exclude = []


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['name','start', 'end', 'details','color']

