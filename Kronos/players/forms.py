from .models import Players
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django import forms


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'surname', 'gaming_number', 'amplua', 'image', 'description']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'pattern': '[A-Za-zА-Яа-яЁё]+'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'pattern': '[A-Za-zА-Яа-яЁё]+'
            }),
            "gaming_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Игровой номер',
                'max': 99
            }),
            'amplua': forms.Select(attrs={
                'class': 'form-control'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание игрока'
            })
        }

    def clean_amplua(self):
        amplua = self.cleaned_data.get('amplua')
        if amplua == 'Выберите амплуа':
            raise forms.ValidationError("Недопустимое значение")
        return amplua