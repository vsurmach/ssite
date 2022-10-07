from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    fname = models.CharField(max_length=10)

    def __str__(self):
        return self.fname


class FaceBook(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)