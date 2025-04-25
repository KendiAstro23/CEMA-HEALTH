from django.db import models

class HealthProgram(models.Model):
    title = models.CharField(max_length=100)

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrolled_programs = models.ManyToManyField(HealthProgram, blank=True)
