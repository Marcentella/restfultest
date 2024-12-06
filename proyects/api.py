from proyects.models import Proyect, Task
from rest_framework import viewsets, permissions
from .serializers import ProyectSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectSerializer     

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    