from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario 

class UsuarioRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")
        #labels = {
        #    'username': ('Nombre de Usuario'),}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 10:
            raise ValidationError("contraseña minima 10 caracteres")
         # TODO Validation
    
        return password1

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
    
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }