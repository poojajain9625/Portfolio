from django.core import validators
from django import forms
from .models import User

class StudentRegisteration(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model=User
        fields=['id','name','email','subject','message']
       