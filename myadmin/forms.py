from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Company


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput())

class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model=Company
        exclude = ["user"]