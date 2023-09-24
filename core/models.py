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
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='projectCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='projectUpdatedBy', null=False, blank=False, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

# PREGUNTAS
class Question(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la pregunta', null=False, blank=False, default='Pregunta')
    text = models.TextField(max_length=500, verbose_name='Texto de la pregunta', null=False, blank=False)
    order = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='questionCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='questionUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

# RESPUESTAS
class Answer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la respuesta', null=False, blank=False, default='Respuesta')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Pregunta', null=False, blank=False, default=1)
    TYPE_CHOICES = [
        ('checkbox', 'Checkbox'),
        ('radiobutton', 'Radio Button'),
    ]
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default='checkbox',
    )
    text = models.TextField(max_length=500, verbose_name='Texto de la respuesta', null=False, blank=False)
    order = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='answerCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='answerUpdatedBy', null=False, blank=False, default=1)
    


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'