from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, TextInput
from .models import Trabajo

class TrabajoForm(forms.ModelForm):
    
    class Meta:
        model = Trabajo
        fields = ('__all__')
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_desde':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fecha_hasta':forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre)<6:
            raise ValidationError("el nombre debe tener al menos 6 caracteres")
    
         # TODO Validation
    
        return nombre