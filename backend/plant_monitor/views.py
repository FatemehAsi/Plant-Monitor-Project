from rest_framework import viewsets
from .models import Plant, HealthStatus
from .serializers import PlantSerializer, HealthStatusSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Plant Monitoring System!"})

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class HealthStatusViewSet(viewsets.ModelViewSet):
    queryset = HealthStatus.objects.all()
    serializer_class = HealthStatusSerializer


