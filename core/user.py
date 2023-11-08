from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=30,
        required=True,  # This makes the field required
        label='Nombre',
        widget=forms.TextInput(attrs={'data-toggle': 'tooltip', 'title': 'Requerido. Ingrese su nombre'})
    )
    
    last_name = forms.CharField(
        max_length=30,
        required=True,  # This makes the field required
        label='Apellido',
        widget=forms.TextInput(attrs={'data-toggle': 'tooltip', 'title': 'Requerido. Ingrese su apellido'})
    
    )
    
    email = forms.EmailField(
        max_length=80,
        required=True,  # This makes the field required
        label='Correo electrónico',
        widget=forms.TextInput(attrs={'data-toggle': 'tooltip', 'title': 'Requerido. Ingrese su correo electrónico'})
    )

    username = forms.CharField(
        max_length=50,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'data-toggle': 'tooltip', 'title': 'Requerido. 50 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_'})
    )

    password1 = forms.CharField(
        max_length=128,
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'data-toggle': 'tooltip', 'title': 'Su contraseña no puede asemejarse tanto a su otra información personal.\nSu contraseña debe contener al menos 8 caracteres.\nSu contraseña no puede ser una clave utilizada comúnmente.\nSu contraseña no puede ser completamente numérica.'}),
    )

    password2 = forms.CharField(
        max_length=128,
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'data-toggle': 'tooltip', 'title': 'Requerido. Confirme su contraseña.'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        
        if 'javascript' in email:
            raise forms.ValidationError("Por favor, ingrese un correo electrónico válido.")
        if 'script' in email:
            raise forms.ValidationError("Por favor, ingrese un correo electrónico válido.")
        
        email = self.cleaned_data.get('email')
        email = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], email)
       
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if 'javascript' in first_name:
            raise forms.ValidationError("Por favor, ingrese un nombre válido.")
        if 'script' in first_name:
            raise forms.ValidationError("Por favor, ingrese un nombre válido.")

        first_name = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], first_name)
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if 'javascript' in last_name:
            raise forms.ValidationError("Por favor, ingrese un apellido válido.")
        if 'script' in last_name:
            raise forms.ValidationError("Por favor, ingrese un apellido válido.")
        
        last_name = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], last_name)
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya existe.')
        
        if 'javascript' in username:
            raise forms.ValidationError("Por favor, ingrese un nombre de usuario válido.")
        if 'script' in username:
            raise forms.ValidationError("Por favor, ingrese un nombre de usuario válido.")
        
        username = re.sub(r'[&<>"\'\?/ ]', lambda x: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;', '?': '&#63;', '/': '&#47;', ' ': '&#32;'}[x.group()], username)
        return username



    
        
        