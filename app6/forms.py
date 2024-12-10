from django.forms import ModelForm
from app6.models import StudyTable
from django import forms
class table(ModelForm):
    class Meta:
        model=StudyTable
        fields="__all__"

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)