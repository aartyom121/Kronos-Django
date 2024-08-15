from django import forms
from .models import Test, Question
from django.forms import ModelForm, TextInput
from users.models import User


class QuestionsForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'cor_ans', 'uncor_ans1',
                  'uncor_ans2', 'uncor_ans3', 'test_number']
        widgets = {
            "question": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос'
            }),
            "cor_ans": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корректный ответ'
            }),
            "uncor_ans1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Некорректный ответ 1'
            }),
            "uncor_ans2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Некорректный ответ 2'
            }),
            "uncor_ans3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Некорректный ответ 3'
            }),
            'test_number': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class TestsForm(ModelForm):
    class Meta:
        model = Test
        fields = ['name']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название теста'
            })
        }
