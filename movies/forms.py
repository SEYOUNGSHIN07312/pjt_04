from django import forms
from .models import Movie
from django.forms import NumberInput, DateInput

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        widgets = {
            'score' : NumberInput(attrs={
                'step' : 0.5,
                'min' : 0,
                'max' : 5,
                }
            ),
            'release_date' : DateInput(attrs={
                'type' : 'date',
            })
        }