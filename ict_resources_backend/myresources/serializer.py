from rest_framework import serializers

from myresources.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id_course', 'start', 'end', 'id_level', 'id_classe', 'pk', 'id_teacher', 'type_reservation',
                  'id_type', 'id_etat', 'id_user']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        exclude = []


class CategorieNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieNotifications
        exclude = []


class TypeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSchedule
        exclude = []


class ReservationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationSchedule
        fields = ['id_schedule', 'id_teacher', 'id', 'message']


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = []


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        exclude = []


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = []


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
