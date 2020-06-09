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

User = settings.AUTH_USER_MODEL


class Adress(models.Model):
    code_postal = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    code_course = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.code_course


class CategoryCourse(models.Model):
    group = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)


class Classe(models.Model):
    code_classe = models.CharField(max_length=20, unique=True)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.code_classe


class CategoryClasse(models.Model):
    department_name = models.CharField(max_length=50)
    classe = models.ManyToManyField(Classe)

    def __str__(self):
        return self.department_name


class Equipment(models.Model):
    equipment = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.equipment


class Schedule(models.Model):
    start = models.CharField(blank=False, null=False, max_length=255)
    end = models.CharField(blank=False, null=False, max_length=55)
    color = models.CharField(max_length=255, default="1976d2")
    is_valid = models.BooleanField(default=False, blank=False)
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=False, null=False)
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, blank=True, null=True)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=False, null=False)


class ReservationSchedule(models.Model):
    id_schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    id_teacher = models.ForeignKey(Teacher,unique=False, on_delete=models.CASCADE)
    is_failed = models.BooleanField(default=False)
    message = models.TextField(default="Reservation en attente")

    def __str__(self):
        return "Reservation pour " + self.id_schedule.id_classe.code_classe


class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=10, unique=True, blank=False)
    is_student = models.BooleanField(default=False)


class Borrow(models.Model):
    date_borrow = models.DateTimeField(default=timezone.now)
    date_delivery = models.DateTimeField(default=timezone.now)
    teacher = models.ManyToManyField(Teacher)
    equipment = models.ManyToManyField(Equipment)


class ReservationEquipment(models.Model):
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    number = models.IntegerField(blank=False, null=False)


class Follow(models.Model):
    matricule_student = models.ForeignKey(Students, on_delete=models.CASCADE)
    code_course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Borrowing(models.Model):
    matricule_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    number = models.ForeignKey(Borrow, on_delete=models.CASCADE)


class Dispense(models.Model):
    matricule_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    code_course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Concern(models.Model):
    code_materiel = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    numero = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
