from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.generics import RetrieveAPIView
from .models import Client, HealthProgram, Appointment
from .serializers import ClientSerializer, HealthProgramSerializer, AppointmentSerializer
from rest_framework import generics


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

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def create(self, request):
        try:
            client_id = request.data['client']
            program_id = request.data['program']
            doctor = request.data.get('doctor', '')
            date = request.data.get('date', None)
            notes = request.data.get('notes', '')

            client = Client.objects.get(id=client_id)
            program = HealthProgram.objects.get(id=program_id)  # 🔥 Use HealthProgram because that's your model name

            appointment = Appointment.objects.create(
                client=client,
                program=program,
                doctor=doctor,
                date=date,
                notes=notes
            )

            # Serialize the newly created appointment
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        except HealthProgram.DoesNotExist:
            return Response({"error": "Program not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PublicClientProfileView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [HasAPIKey]

@api_view(['GET'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client)
    return Response(serializer.data)