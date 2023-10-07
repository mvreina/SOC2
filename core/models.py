from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import uuid
from multiselectfield import MultiSelectField

# PREGUNTAS
class Question(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la pregunta', null=False, blank=False, default='Pregunta')
    text = models.TextField(max_length=500, verbose_name='Texto de la pregunta', null=False, blank=False)
    orderQuestion = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    TYPE_CHOICES = [
        ('checkbox', 'Checkbox'),
        ('radiobutton', 'Radio Button'),
    ]
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default='checkbox',
    )
    
    #Datos del sistema
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
    orderAnswer = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='answerCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='answerUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

def getANSWERS(num):
    ANSWERS = []
    for i in range(1, num+1):
        #ANSWERS.append((str(i), 'Respuesta ' + str(i)))
        ANSWERS.append((str(i), str(i)))

    print(ANSWERS)
    return ANSWERS

def getAnswersDefault(num):
    answers = ""
    for i in range(1, num+1):
        answers += str(i)
        if i < num:
            answers += ","
    
    print(answers)
    return answers

# PROYECTOS
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del proyecto')
    startDate = models.DateField(verbose_name='Fecha inicio')
    endDate = models.DateField(verbose_name='Fecha fin')
    numQuestion = models.IntegerField(verbose_name='Número de pregunta', null=False, default=1)

    #Preguntas
    #question1 = MultiSelectField(choices=getANSWERS(5), max_length=11, default=getAnswersDefault(5))
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='projectCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='projectUpdatedBy', null=False, blank=False, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

# PROYECTO - PREGUNTAS
class ProjectQuestion(models.Model):
    
    #Relacionados
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto', null=False, blank=False, default=1)
    question = models.ManyToManyField(Question)
    answer = models.ManyToManyField(Answer)
    
    userAnswer = models.BooleanField(default=True)
    orderProjectQuestion = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=1)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='project_questionCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='project_questionUpdatedBy', null=False, blank=False, default=1)
    

    
    def __str__(self):
        return self.project.name
    
    class Meta:
        verbose_name = 'Proyecto - Preguntas'
        verbose_name_plural = 'Projectos - Preguntas'



"""
# PROYECTO - RESPUESTAS

class ProjectAnswer(models.Model):
    
    #Relacionados
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto', related_name='project_answer', null=False, blank=False, default=1)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Respuesta', related_name='answer_project', null=False, blank=False, default=1)
    ANSWER_CHOICES = [
        ('TRUE', 'TRUE'),
        ('FALSE', 'FALSE'),
    ]
    userAnswer = models.CharField(
        max_length=12,
        choices=ANSWER_CHOICES,
        default='TRUE',
    )
    #order = models.IntegerField(verbose_name='Orden', null=False, blank=False, default=1)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='project_answerCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='project_answerUpdatedBy', null=False, blank=False, default=1)
    

    
    def __str__(self):
        return self.project.name
    
    class Meta:
        verbose_name = 'Proyecto - Respuestas'
        verbose_name_plural = 'Projectos - Respuestas'
"""