from django import forms
from .models import *

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = PatientCreate
        fields = '__all__'
