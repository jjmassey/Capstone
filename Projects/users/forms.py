from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']

class ProfileRegistrationForm(forms.ModelForm):
    phone_Number = forms.CharField()
    company = forms.CharField()

    class Meta:
        model = Profile
        fields = ['phone_Number', 'company']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'company', 'phone_Number']
