from django import forms
from .models import *

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = PatientCreate
        fields = '__all__'
class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = DoctorCreate
        fields = '__all__'