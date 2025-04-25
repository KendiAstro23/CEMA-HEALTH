from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Client, HealthProgram
from .serializers import ClientSerializer, HealthProgramSerializer


class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    permission_classes = [IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
