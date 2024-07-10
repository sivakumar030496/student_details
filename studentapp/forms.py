
import django
from .models import StudentData
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm


class studentForm(forms.ModelForm):
    class Meta:
        model=StudentData
        fields='__all__'



class UserDetailsForm(forms.Form):
    name=forms.CharField(max_length=20)
    mobile=forms.CharField(max_length=13)
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':22,'rows':4}))
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.name