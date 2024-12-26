from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import WorkoutCompanion
from django.db import models


class UserInputForm(forms.ModelForm):
    class Meta:
        model = WorkoutCompanion
        fields = ['user_first_name', 'user_last_name', 'user_age', 'user_gender', 'user_weight', 'user_height', 'user_workout_choice', 'profile_picture']
        widgets = {
            'user_gender': forms.RadioSelect,
            'user_workout_choice': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_gender'].choices = list(filter(lambda choice: choice[0], self.fields['user_gender'].choices))
        self.fields['user_workout_choice'].choices = list(filter(lambda choice: choice[0], self.fields['user_workout_choice'].choices))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
