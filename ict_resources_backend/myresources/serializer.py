from rest_framework import serializers

from myresources.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id_course', 'start', 'end', 'color', 'id', 'id_classe', 'id_equipment', 'id_teacher', 'is_valid']


class ReservationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationSchedule
        fields = ['id_schedule', 'id_teacher', 'id', 'message']


class CategoryClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryClasse
        exclude = []


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        exclude = []


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['equipment', 'id', 'number']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationEquipment
        fields = ['id_equipment', 'number']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = []


class CategoryCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCourse
        exclude = []
