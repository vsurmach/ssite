from django.db import models


class SchoolPerson(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()


class University(models.Model):
    name = models.CharField(max_length=20)
    student = models.ForeignKey(SchoolPerson, on_delete=models.CASCADE)


class LevakModel(models.Model):
    book = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
