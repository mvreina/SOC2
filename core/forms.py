from django import forms
from .models import Project, Question, Answer, ProjectQuestion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


#PROJECT - QUESTION - ANSWER
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
  

#PROJECT
class ProjectForm(forms.ModelForm):
    print('Fecha actual: ', timezone.now().date())
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

        if start_date and end_date:
            if start_date + relativedelta(months=3) > end_date:
                raise ValidationError("Por favor, ingrese una fecha fin que sea 3 meses posterior a la fecha de inicio.")
                #self.add_error('endDate', "Por favor, ingresa una fecha fin que sea 3 meses posterior a la fecha de inicio.")
                
#ANSWER
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

#QUESTION
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
