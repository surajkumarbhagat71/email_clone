from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

