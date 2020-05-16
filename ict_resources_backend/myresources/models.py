from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.authtoken.models import Token


# Create your models here.

class TokenModel(models.Model):
    pass


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.password


class Adress(models.Model):
    code_postal = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)


class Schedule(models.Model):
    start = models.CharField(blank=False, null=False , max_length=255)
    end = models.CharField(blank=False, null=False, max_length=55)
    details = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    color = models.CharField(max_length=255, default="1976d2")


class Classe(models.Model):
    code_classe = models.CharField(max_length=10, unique=True)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)


class Students(models.Model):
    matricule = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(default=timezone.now)
    address = models.OneToOneField(Adress, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)


class Teacher(models.Model):
    matricule = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_naissance = models.DateTimeField(default=timezone.now)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)


class Category(models.Model):
    category_code = models.CharField(max_length=10, unique=True)
    category_name = models.CharField(max_length=50)


class Equipment(models.Model):
    code_equipment = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Borrow(models.Model):
    date_borrow = models.DateTimeField(default=timezone.now)
    date_delivery = models.DateTimeField(default=timezone.now)
    teacher = models.ManyToManyField(Teacher)
    equipment = models.ManyToManyField(Equipment)


class Room(models.Model):
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    classe = models.ManyToManyField(Classe)


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


class Shelter(models.Model):
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    code_room = models.ForeignKey(Classe, on_delete=models.CASCADE)
