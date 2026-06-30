from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class RegisterForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    rep_password=forms.CharField(widget=forms.PasswordInput())
    role=forms.CharField(choices=User.ROLE_CHOICES)