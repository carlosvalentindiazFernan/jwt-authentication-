from django import forms
from django.forms import Textarea
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields=('name','size')

        widgets={

            'name': forms.TextInput(attrs={
                'class':'form-control'
            }),

            'size': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }