from rest_framework import serializers #Esta biblioteca es una extensión del framework Django que proporciona herramientas y utilidades adicionales para construir APIs web
from .models import Proyect, Task

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id',  'nombre', 'rut', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'project', 'created_at']