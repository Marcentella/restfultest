from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from .models import Task, Proyect
from .serializers import TaskSerializer, ProyectSerializer

# ViewSet para tareas
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# ViewSet para proyectos
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    serializer_class = ProyectSerializer

# Punto de entrada para la raíz de la API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })
