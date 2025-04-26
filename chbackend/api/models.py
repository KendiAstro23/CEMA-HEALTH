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

class Appointment(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='appointments')
    doctor = models.CharField(max_length=100)  # You can later link to a real Doctor model
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.client.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"
