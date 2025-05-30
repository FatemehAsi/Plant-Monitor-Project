from rest_framework import viewsets
from .models import Plant, HealthStatus
from .serializers import PlantSerializer, HealthStatusSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return JsonResponse({"message": "Welcome to the Plant Monitoring System!"})

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class HealthStatusViewSet(viewsets.ModelViewSet):
    queryset = HealthStatus.objects.all()
    serializer_class = HealthStatusSerializer

@api_view(['POST'])
def telemetry_view(request):
    try:
        data = json.loads(request.body)
        plant_id = data.get("plant_id")  # send plant_id from device or ThingsBoard
        humidity = data.get("humidity")
        temperature = data.get("temperature")
        moisture = data.get("moisture")

        plant = Plant.objects.get(id=plant_id)
        
        latest_status = HealthStatus.objects.filter(plant=plant).order_by('status_date').first()
        if latest_status:
            latest_status.humidity = humidity
            latest_status.temperature = temperature
            latest_status.moisture = moisture
            latest_status.save()
            serializer = HealthStatusSerializer(latest_status)
            return JsonResponse({"status": "Updated"}, status=status.HTTP_200_OK)
        else:
            HealthStatus.objects.create(
                plant=plant,
                humidity=humidity,
                temperature=temperature,
                moisture=moisture
            )
            return JsonResponse({"status": "created"},  status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)