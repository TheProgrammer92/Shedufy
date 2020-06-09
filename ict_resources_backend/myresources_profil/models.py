import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


# Create your models here.

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class CustomUser(AbstractUser):
    avatar = models.ImageField(blank=True, null=True, upload_to="users/images")
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    matricule = models.CharField(blank=True, null=True, max_length=10)
    sexe = models.IntegerField(blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
