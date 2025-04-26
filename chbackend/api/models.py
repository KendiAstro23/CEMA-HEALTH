from django.db import models

class HealthProgram(models.Model):
    name = models.CharField(max_length=100)

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    interests = models.TextField(blank=True)
    enrolled_programs = models.ManyToManyField(HealthProgram, blank=True)
