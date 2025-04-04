from .models import A
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms
from django.contrib.auth import get_user_model

class AForm(ModelForm):
    class Meta:
        model = A
        fields = ['title', 'author', 'genre', 'description', 'number_of_copies', 'date']
        widgets = {
            "title":TextInput( attrs={
                'class':'send_input',
                'placeholder':'name letter',
            }),
            "author": TextInput(attrs={
                'class': 'send_input',
                'placeholder': 'write the author',
            }),
            "genre": TextInput(attrs={
                'class': 'send_input',
                'placeholder': 'write the genre',
            }),
            "description": TextInput( attrs={
                'class':'send_input',
                'placeholder':'description book',
            }),
            "number_of_copies": TextInput(attrs={
                'class': 'send_input',
                'placeholder': 'quantity'
            }),
            "date":TextInput( attrs={
                'class':'send_input',
                 'placeholder':'date'
            })
        }