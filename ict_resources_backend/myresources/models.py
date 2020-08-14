from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone

from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
# Create your models here.
from django.conf import settings
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Course(models.Model):
    code_course = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    praticals_works = models.BooleanField(default=False)

    def __str__(self):
        return self.code_course


class CategoryCourse(models.Model):
    group = models.CharField(max_length=50)
    course = models.ManyToManyField(Course, symmetrical=True)


class Level(models.Model):
    level_number = models.IntegerField(blank=False, null=False)
    level_code = models.CharField(max_length=20, blank=False, null=False)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return str(self.level_code)


class FiliereCategorie(models.Model):
    faculty_type = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.faculty_type


class Filiere(models.Model):
    filiere_name = models.CharField(max_length=100, blank=False, null=False)
    filiere_code = models.CharField(max_length=100, blank=False, null=False)
    filiere_categorie = models.OneToOneField(FiliereCategorie, on_delete=models.CASCADE, null=True, blank=True)
    id_level = models.ManyToManyField(Level)

    def __str__(self):
        return self.filiere_name


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    filiere = models.ManyToManyField(Filiere)

    def __str__(self):
        return self.department_name


class Classe(models.Model):
    code_classe = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.code_classe


class CategoryClasse(models.Model):
    categorie_name = models.CharField(max_length=50)
    classes = models.ManyToManyField(Classe)

    def __str__(self):
        return self.categorie_name


class Equipment(models.Model):
    equipment = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.equipment


class TypeSchedule(models.Model):
    class TypeSchedule(models.TextChoices):
        CC = 'CC', _('CC')
        SN = 'SN', _('Session Normale')
        COURS = 'COURS', _('COURS')
        RATTRAPPAGE = 'RATTRAPPAGE', _('RATTRAPPAGE')
        TD = 'TD', _('TD')
        TP = 'TP', _('TP')

    type = models.CharField(max_length=20, choices=TypeSchedule.choices, default=TypeSchedule.COURS, unique=True)
    color = models.CharField(max_length=255, default="1976d2")

    def __str__(self):
        return self.type


class Schedule(models.Model):
    start = models.CharField(blank=False, null=False, max_length=255)
    end = models.CharField(blank=False, null=False, max_length=55)
    is_valid = models.BooleanField(default=False, blank=False)
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=False, null=True)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=True)
    id_teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    id_level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=False, null=True)
    id_type = models.ForeignKey(TypeSchedule, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.start + " " + self.end


class ReservationSchedule(models.Model):
    id_schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, null=True)
    is_failed = models.BooleanField(default=False)
    message = models.TextField(default="Reservation en attente")

    def __str__(self):
        return "Reservation pour " + self.id_schedule.id_classe.code_classe


class Borrow(models.Model):
    date_borrow = models.DateTimeField(default=timezone.now)
    date_delivery = models.DateTimeField(default=timezone.now)
    equipment = models.ManyToManyField(Equipment)


class ReservationEquipment(models.Model):
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(blank=False, null=False)
