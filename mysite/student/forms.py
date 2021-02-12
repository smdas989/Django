from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomStudentModel

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    standard = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    roll_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    
    gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

