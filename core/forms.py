from django import forms
from .models import *

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = PatientCreate
        fields = '__all__'
        widgets = {
            'patient_fullname': forms.TextInput(attrs={'class':'form-control'}),
            'patient_phone': forms.NumberInput(attrs={'class':'form-control'}),
            'patient_address':forms.TextInput(attrs={'class':'form-control'}),
            'patient_age':forms.NumberInput(attrs={'class':'form-control'}),
            'patient_blood':forms.Select(attrs={'class':'form-control'}),
            'patient_status':forms.Select(attrs={'class':'form-control'}),
            'patient_married':forms.Select(attrs={'class':'form-control'}),
            'patient_gender':forms.Select(attrs={'class':'form-control'}),
            'patient_acceptance':forms.Select(attrs={'class':'form-control'}),
            'patient_discription':forms.Textarea(attrs={'class':'form-control'}),
            'check_in_date':forms.SplitDateTimeWidget(),
            'diseases':forms.TextInput(attrs={'class':'form-control'}),
            'patient_room':forms.Select(attrs={'class':'form-control'}),
           


        }
class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = DoctorCreate
        fields = '__all__'