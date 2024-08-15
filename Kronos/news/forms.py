from django import forms

from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ModelChoiceField

from users.models import User


class ArticlesForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            # "date": DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Дата публикации'
            #
            # }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }