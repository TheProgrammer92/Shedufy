import os

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from django.conf import settings

from functions.functions import generate_url, send_activate_account_mail

User = settings.AUTH_USER_MODEL

from .constants import *


# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (ADMIN, 'admin'),
        (SUPERADMIN, 'super admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    department = models.ForeignKey('myresources.Department', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_id_display()


class CustomUser(AbstractUser):
    """
        Stores a single blog entry, related to :model:`blog.Blog` and
        :model:`auth.User`.
        """
    username = models.CharField(blank=True, null=True, max_length=150)
    avatar = models.ImageField(blank=True, null=True, upload_to="users/images")
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    matricule = models.CharField(blank=True, null=True, max_length=10)
    sexe = models.IntegerField(blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    profile = models.ManyToManyField(Profile)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class CodeValidation(models.Model):
    """
    Validation  de code pour les inscriptions  , voici le format , les url qui commencent par :
    STU- = Etudiant
    TEACH- = Teacher
    SECR-= Secretaire
    ADMIN- =- ADMIN
    SUPER- = Super admin
    """
    id_creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    url_code = models.CharField(blank=False, null=False, max_length=10)
    date_expiration = models.DateTimeField(blank=False, null=False)
    is_valid = models.BooleanField(blank=False, null=False, default=False)
