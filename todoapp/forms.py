from django import forms
from .models import TodoApp


class TodoAppForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['id', 'name', 'text']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = TodoApp
        fields = ['name', 'text']
        exclude = ('created_at',)
