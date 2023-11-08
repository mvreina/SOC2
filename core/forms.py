from django import forms
from .models import Project, Question, Answer, ProjectQuestion, Text, ProjectPolicy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
import re
    

#PROYECTO - PREGUNTA - RESPUESTA
class ProjectQuestionForm(forms.ModelForm):
    class Meta:
        model = ProjectQuestion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectQuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('project'),
            Field('question'),
            Field('answer'),
            Field('userAnswer'),
            Submit('submit', 'Guardar')
        )
  

#PROYECTO
class ProjectForm(forms.ModelForm):
    #print('Fecha actual: ', timezone.now().date())
    startDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}), initial=str(timezone.now().date()), label='Fecha inicio')
    endDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}), initial=str(timezone.now().date()+ relativedelta(months=3)), label='Fecha fin')

    class Meta:
        model = Project
        fields = ['name', 'startDate', 'endDate']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name'),
        Field('startDate'),
        Field('endDate'),
        Submit('submit', 'Guardar')
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("startDate")
        end_date = cleaned_data.get("endDate")
        name = cleaned_data.get("name")

        if start_date and end_date:
            if start_date + relativedelta(months=3) > end_date:
                raise ValidationError("Por favor, ingrese una fecha fin que sea 3 meses posterior a la fecha de inicio.")
                #self.add_error('endDate', "Por favor, ingresa una fecha fin que sea 3 meses posterior a la fecha de inicio.")

        if 'javascript' in name:
            raise ValidationError("Por favor, ingrese un nombre de proyecto válido.")
        if 'script' in name:
            raise ValidationError("Por favor, ingrese un nombre de proyecto válido.")
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], name)
        return name
    

#RESPUESTA
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

#PREGUNTA
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

#DOCUMENTOS
class TextForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = ['content']

class TextProjectPolicyForm(forms.ModelForm):

    STATUS_CHOICES = (
        ('Borrador', 'Borrador'),
        ('Aprobado', 'Aprobado'),
        ('Descontinuado', 'Descontinuado'),
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    ) 

    class Meta:
        model = ProjectPolicy
        fields = ['content', 'status']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        
        if 'javascript' in content:
            raise ValidationError("Por favor, ingrese un documento válido.")
        if 'script' in content:
            raise ValidationError("Por favor, ingrese un documento válido,")
        
        #content = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], content)
        return content
    
    def clean_status(self):
        status = self.cleaned_data.get('status')
        
        if 'javascript' in status:
            raise forms.ValidationError("Por favor, ingrese un estado válido.")
        if 'script' in status:
            raise forms.ValidationError("Por favor, ingrese un estado válido.")
        
        status = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], status)
        return status