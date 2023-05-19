from django import forms
from .models import Create


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = ['name', 'email', 'phone']