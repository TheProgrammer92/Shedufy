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

from myresources_profil.constants import *

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
    ROLE_CHOICES = (
        (COURS, 'cours'),
        (CC, 'cc'),
        (RATTRAPAGE, 'rattrapage'),
        (TD, 'TD'),
        (SN, 'sn'),
        (RESERVATION, 'reservation'),
        (TEACHER_TYPE, 'teacher'),
    )

    type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=COURS, unique=True)
    color = models.CharField(max_length=255, default="blue")
    value = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return str(self.type) + " " + self.value


# les differents état d'un schedule pour la reservation
class Etat(models.Model):
    ROLE_CHOICES = (
        (ETAT_VALIDE, 'validé'),
        (ETAT_ANNULLE, 'annulté'),
        (ETAT_REFUS, 'refusé'),
        (ETAT_ATTENTE, 'en attente'),
    )

    etat = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True, default=ETAT_VALIDE)

    def __str__(self):
        return str(self.pk) + " " + self.get_etat_display()


class Schedule(models.Model):
    start = models.CharField(blank=False, null=False, max_length=255)
    end = models.CharField(blank=False, null=False, max_length=55)
    id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, blank=False, null=False)
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    id_teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    id_level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=False, null=False)
    id_type = models.ForeignKey(TypeSchedule, to_field="type", on_delete=models.CASCADE, blank=False, null=False)
    id_etat = models.ForeignKey(Etat, on_delete=models.CASCADE, default=ETAT_VALIDE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                                related_name="id_user_schedule")
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type_reservation = models.ForeignKey(TypeSchedule, to_field="type", on_delete=models.CASCADE, default=COURS, blank=False, null=False,
                                         related_name="type_reservation")  # pour identifier le type de reservation pour le prof

    def __str__(self):
        return self.start + " " + self.end


# - envoyer les messages par mail, et aux professeur(q
# uand un nouveau cours lui est attribué et quand on valide la réservation)
# - notifier un admin quand un prof a demandé une réservation, .

class CategorieNotifications(models.Model):
    ROLE_CHOICES = (
        (COURS, 'cours'),
        (CC, 'cc'),
        (RATTRAPAGE, 'rattrapage'),
        (TD, 'TD'),
        (SN, 'sn'),
        (RESERVATION, 'reservation'),
    )

    type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=COURS, unique=True)
    value = models.CharField(max_length=255, default="cours")

    def __str__(self):
        return self.get_type_display()


class Notifications(models.Model):
    id_event = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=200)
    id_cat = models.ForeignKey(CategorieNotifications, on_delete=models.CASCADE, to_field="type")
    id_emetter = models.ForeignKey(User, on_delete=models.CASCADE)
    id_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_notification")

    def __str__(self):
        return str(self.pk) + " " + self.message


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
