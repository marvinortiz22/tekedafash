from django import forms
from Administrador.models import *
class PerfilForm(forms.ModelForm):
    nacimiento=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        fields=['username','first_name','last_name','email','documento','nacimiento'] 
        model=Usuario

