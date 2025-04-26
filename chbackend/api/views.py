from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, HealthProgram
from .serializers import ClientSerializer, HealthProgramSerializer


class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

@api_view(['GET'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client)
    return Response(serializer.data)