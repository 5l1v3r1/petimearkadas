from django import forms
from .models import Pet,Post

__author__ = 'frkn'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class PetCreationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ("name", "age", "kind", "gender", "is_barren", "image", "user")


class AdvertCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "location", "pet", "user")








