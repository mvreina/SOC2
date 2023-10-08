from django import forms
from .models import Project, Question, Answer, ProjectQuestion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
import django_tables2 as tables
from django.forms import BaseInlineFormSet, inlineformset_factory
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


#PROJECT - QUESTION - ANSWER
class ProjectQuestionForm(forms.ModelForm):
    class Meta:
        model = ProjectQuestion
        #fields = ['project', 'question', 'answer', 'userAnswer', 'order']
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
    startDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha inicio', initial=timezone.now)
    endDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha fin')

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
