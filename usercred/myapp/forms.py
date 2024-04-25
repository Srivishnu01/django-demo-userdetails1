from django import forms
from .models import CustomUser, Profile


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'mypassword']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'created_datetime']
