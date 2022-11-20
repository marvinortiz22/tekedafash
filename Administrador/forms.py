from django.contrib.auth.forms import UserChangeForm
from django import forms
from Administrador.models import *
class PerfilForm(UserChangeForm):
    class Meta:
        fields=['username','first_name','last_name','email','documento','nacimiento']
        model=Usuario