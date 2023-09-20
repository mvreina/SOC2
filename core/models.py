from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.utils import timezone

# PROYECTOS
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del proyecto')
    startDate = models.DateField(verbose_name='Fecha inicio')
    endDate = models.DateField(verbose_name='Fecha fin')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='createdBy', null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

