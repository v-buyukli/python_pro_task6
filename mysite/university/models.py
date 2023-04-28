from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birthdate = models.DateField()
    subject = models.CharField(max_length=100)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
