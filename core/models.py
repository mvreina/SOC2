from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField


# PREGUNTAS
class Question(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la pregunta', null=False, blank=False, default='Pregunta')
    text = models.TextField(max_length=500, verbose_name='Texto de la pregunta', null=False, blank=False)
    orderQuestion = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=0)
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
    text = models.TextField(max_length=610, verbose_name='Texto de la respuesta', null=False, blank=False)
    orderAnswer = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    policyOptions = [] 
    for i in range(1, 33):
        policyOptions.append((i, f'Política {i}'))

    excludedPolicies = MultiSelectField(choices=policyOptions, max_length=100, verbose_name='Políticas excluidas', blank=True, null=True, default=[1])

    controlOptions = [] 
    for i in range(1, 409):
        controlOptions.append((i, f'Control {i}'))

    excludedControls = MultiSelectField(choices=controlOptions, max_length=100, verbose_name='Controles excluidos', blank=True, null=True)
    
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

# PROYECTOS
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del proyecto')
    startDate = models.DateField(verbose_name='Fecha inicio')
    endDate = models.DateField(verbose_name='Fecha fin')
    numQuestion = models.PositiveIntegerField(verbose_name='Número de pregunta', null=False, default=1)
    
    policyOptions = [] 
    for i in range(1, 33):
        policyOptions.append((i, f'Política {i}'))

    excludedPolicies = MultiSelectField(choices=policyOptions, max_length=100, verbose_name='Políticas excluidas', blank=True, null=True)
    
    controlOptions = [] 
    for i in range(1, 409):
        controlOptions.append((i, f'Control {i}'))

    excludedControls = MultiSelectField(choices=controlOptions, max_length=200, verbose_name='Controles excluidos', blank=True, null=True)
    


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
    orderProjectQuestion = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=1)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='project_questionCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='project_questionUpdatedBy', null=False, blank=False, default=1)
    

    
    def __str__(self):
        return self.project.name
    
    class Meta:
        verbose_name = 'Proyecto - Preguntas'
        verbose_name_plural = 'Proyectos - Preguntas'


#POLITICAS
class Policy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la política', null=False, blank=False, default='Política')
    category = models.CharField(max_length=200, verbose_name='Categoría', null=False, blank=False, default='Categoría')
    orderPolicy = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='policyCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='policyUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Política'
        verbose_name_plural = 'Políticas'


# PROYECTO - POLITICAS
class ProjectPolicy(models.Model):
    
    #Relacionados
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto', null=False, blank=False, default=1)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, verbose_name='Política', null=False, blank=False, default=1)
        
    excluded = models.BooleanField(default=False)
    orderProjectPolicy = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=1)
    STATUS_CHOICES = [
        ('Borrador', 'Borrador'),
        ('Aprobado', 'Aprobado'),
        ('Descontinuado', 'Descontinuado'),
    ]
    status = models.CharField(
        max_length=13,
        choices=STATUS_CHOICES,
        default='Borrador',
        verbose_name='Estado',
    )
    
    #Documento
    content = RichTextField(blank=True, null=True)
    fileName = models.CharField(max_length=200, verbose_name='Nombre del archivo', null=False, blank=False, default='Archivo')

    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='project_policyCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='project_pUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.project.name
    
    class Meta:
        verbose_name = 'Proyecto - Políticas'
        verbose_name_plural = 'Proyectos - Políticas'


#CONTROLES
class Control(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del control', null=False, blank=False, default='Control')
    description = models.CharField(max_length=450, verbose_name='Descripción Breve', null=False, blank=False, default='Descripción')
    moreThanOnePolicy = models.BooleanField(default=False, verbose_name='¿Aplica en más de una Política?')
    howMany = models.PositiveIntegerField(verbose_name='¿Cuantas?', null=False, blank=False, default=1)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, verbose_name='Política', null=False, blank=False, default=1)
    orderControl = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=0)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='controlCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='controlUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Control'
        verbose_name_plural = 'Controles'


# PROYECTO - POLITICAS
class ProjectControl(models.Model):
    
    #Relacionados
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto', null=False, blank=False, default=1)
    control = models.ForeignKey(Control, on_delete=models.CASCADE, verbose_name='Control', null=False, blank=False, default=1)
        
    excluded = models.BooleanField(default=False)
    orderProjectControl = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=1)

    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='project_controlCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='project_controlUpdatedBy', null=False, blank=False, default=1)
    
    def __str__(self):
        return self.project.name
    
    class Meta:
        verbose_name = 'Proyecto - Controles'
        verbose_name_plural = 'Proyectos - Controles'


# DOCUMENTOS
class Text(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre de la política', null=False, blank=False, default='Política')
    fileName = models.CharField(max_length=200, verbose_name='Nombre del archivo', null=False, blank=False, default='Archivo')
    orderText = models.PositiveIntegerField(verbose_name='Orden', null=False, blank=False, default=1)
    content = RichTextField(blank=True, null=True)
    
    #Datos del sistema
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creado por', related_name='textCreatedBy', null=False, blank=False, default=1)
    updatedBy = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Actualizado por', related_name='textUpdatedBy', null=False, blank=False, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
