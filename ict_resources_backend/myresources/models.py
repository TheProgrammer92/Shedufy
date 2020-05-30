from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TokenModel(models.Model):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(blank=True, null=True, upload_to="users/avatars/")
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Adress(models.Model):
    code_postal = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)


class Classe(models.Model):
    code_classe = models.CharField(max_length=20, unique=True)


class Equipment(models.Model):
    equipment = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(blank=False, null=False)


class Schedule(models.Model):
    start = models.CharField(blank=False, null=False, max_length=255)
    end = models.CharField(blank=False, null=False, max_length=55)
    details = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    color = models.CharField(max_length=255, default="1976d2")
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)


class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=10, unique=True, blank=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=10, unique=True, blank=False)
    is_teacher = models.BooleanField(default=False)


class Borrow(models.Model):
    date_borrow = models.DateTimeField(default=timezone.now)
    date_delivery = models.DateTimeField(default=timezone.now)
    teacher = models.ManyToManyField(Teacher)
    equipment = models.ManyToManyField(Equipment)


class ReservationEquipment(models.Model):
    id_equipment: Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, unique=True)
    number = models.IntegerField(blank=False, null=False)


class Course(models.Model):
    code_course = models.CharField(max_length=10, unique=True)
    entitled = models.CharField(max_length=50)
    student = models.ManyToManyField(Students)
    teacher = models.ManyToManyField(Teacher)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)


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
