from .models import News, Category
from django.forms import ModelForm, TextInput, Textarea, Select


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введение название новости',
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введение текст новости',
                'rows': '10'
            }),
            'category': Select(attrs={
                'class': 'form-control',
            })

        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введение название новой категории',
            }),
        }
