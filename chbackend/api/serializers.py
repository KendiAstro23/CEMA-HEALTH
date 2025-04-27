from rest_framework import serializers
from .models import Client, HealthProgram, Appointment

class ClientSerializer(serializers.ModelSerializer):
    enrolled_programs = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'age', 'interests', 'image_url', 'enrolled_programs']


class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']


class AppointmentSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    program_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = [
            'id',
            'client', 'client_name',
            'program', 'program_name',
            'doctor',
            'date',
            'notes'
        ]

    def get_client_name(self, obj):
        return obj.client.name if obj.client else ""

    def get_program_name(self, obj):
        return obj.program.name if obj.program else ""
