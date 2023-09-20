from django import forms
from .models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class ProjectForm(forms.ModelForm):
    startDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha inicio')
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