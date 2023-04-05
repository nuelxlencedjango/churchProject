from dataclasses import fields
#from tkinter import Widget
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')



class UserDetailForm(forms.ModelForm):
    class Meta:
        model = GrowthTrackRegistration
        fields = ('phone_no',)



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')