#coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class ResUser(models.Model):
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    password=models.CharField(max_length=16)
    email = models.EmailField(_('email address'), blank=True)
    phone = models.CharField(max_length=13)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)