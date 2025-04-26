from rest_framework import serializers
from .models import Client, HealthProgram, Appointment

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    enrolled_programs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Client
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'client', 'client_name', 'doctor', 'date', 'notes']
