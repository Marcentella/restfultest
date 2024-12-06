from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TaskViewSet, ProjectViewSet
from .views import api_root  # Importa la vista de la raíz de la API

# Configuración del router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')  # Registrar tasks
router.register(r'projects', ProjectViewSet, basename='project')  # Registrar projects

# URLs
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas de la API
]