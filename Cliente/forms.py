from django import forms
from Administrador.models import *

class PerfilForm(forms.ModelForm):
    nacimiento=forms.DateField(widget=forms.TextInput(attrs={"type":"date","class":"form-control"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    documento=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    class Meta:
        fields=['username','first_name','last_name','email','documento','nacimiento'] 
        model=Usuario

