from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, HealthStatusViewSet, home, telemetry_view

router = DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'health', HealthStatusViewSet)

urlpatterns = [
    path('', home),
    path('', include(router.urls)),
    path('api/telemetry/', telemetry_view),
]
