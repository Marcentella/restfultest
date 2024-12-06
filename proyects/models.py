from django.db import models

# Create your models here.
class Proyect(models.Model):
  rut = models.CharField(max_length=200, default='Sin RUT')
  nombre = models.CharField(max_length=200, default='Sin Nombre')
  title = models.CharField(max_length=200)
  description = models.TextField()
  technology = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Proyect', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title







  