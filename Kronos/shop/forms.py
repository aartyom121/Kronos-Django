from .models import Product
from django.forms import ModelForm, TextInput, NumberInput
from django import forms


class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'image']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
                # 'pattern': '[A-Za-zА-Яа-яЁё]+'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),

        }
    #
    # def clean_amplua(self):
    #     amplua = self.cleaned_data.get('amplua')
    #     if amplua == 'Выберите амплуа':
    #         raise forms.ValidationError("Недопустимое значение")
    #     return amplua