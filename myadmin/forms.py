from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput())

class CompanyRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','is_admin']