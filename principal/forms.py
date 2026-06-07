from django import forms
from .models import ubicacion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = ubicacion
        fields = ['latitud', 'longitud']

        widgets = {
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: -33.4489',
                'step': 'any'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: -70.6693',
                'step': 'any'
            }),
        }