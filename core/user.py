from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        return email