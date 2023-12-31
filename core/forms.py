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
            'patient_birth':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'patient_blood':forms.Select(attrs={'class':'form-control'}),
            'patient_status':forms.Select(attrs={'class':'form-control'}),
            'patient_married':forms.Select(attrs={'class':'form-control'}),
            'patient_gender':forms.Select(attrs={'class':'form-control'}),
            'patient_acceptance':forms.Select(attrs={'class':'form-control'}),
            'patient_discription':forms.Textarea(attrs={'class':'form-control'}),
            'check_in_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'diseases':forms.TextInput(attrs={'class':'form-control'}),
            'patient_room':forms.Select(attrs={'class':'form-control'}),
        }
class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = DoctorCreate
        fields = ['profile_image','muqova_image','doctor_fullname','doctor_phone','doctor_address','doctor_age','doctor_birth','doctor_blood','doctor_status','doctor_university','doctor_discription','doctor_skills','work_time','email_address']
        widgets = {
            'doctor_fullname': forms.TextInput(attrs={'class':'form-control'}),
            'doctor_phone': forms.NumberInput(attrs={'class':'form-control'}),
            'doctor_address':forms.TextInput(attrs={'class':'form-control'}),
            'doctor_age':forms.NumberInput(attrs={'class':'form-control'}),
            'doctor_birth':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'doctor_blood':forms.Select(attrs={'class':'form-control'}),
            'doctor_status':forms.Select(attrs={'class':'form-control'}),
            'doctor_university':forms.Textarea(attrs={'class':'form-control'}),
            'doctor_discription':forms.Textarea(attrs={'class':'form-control'}),
            'doctor_skills':forms.Select(attrs={'class':'form-control'}),
            'work_time':forms.TimeInput(attrs={'type': 'time', 'class':'form-control'}),
            'email_address' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':"saragraham101@gmail.com" }),
            'profile_image' : forms.ClearableFileInput( attrs={'class':'form-file'}),
            "muqova_image": forms.ClearableFileInput(attrs={'class':'form-file'}),
        }

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'
        widgets = {
            'patient_fullname': forms.Select(attrs={'class':'form-control' }),
            'operatsion_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'operatsion_time':forms.TimeInput(attrs={'type': 'time', 'class':'form-control'}),
            'select_operatsion_type':forms.Select(attrs={'class':'form-control wide'}),
            'operatsion_price':forms.NumberInput(attrs={'class':'form-control'}),
            'paid_amount':forms.NumberInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control  message'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientCreate
        fields = ['patient_fullname', 'patient_phone', 'patient_address', 'patient_birth', 'patient_age', 'patient_blood', 'patient_status', 'patient_married', 'patient_gender', 'patient_acceptance', 'patient_discription', 'check_in_date', 'diseases', 'patient_room']
        widgets = {
            'patient_fullname': forms.TextInput(attrs={'class':'form-control'}),
            'patient_phone': forms.NumberInput(attrs={'class':'form-control'}),
            'patient_address':forms.TextInput(attrs={'class':'form-control'}),
            'patient_age':forms.NumberInput(attrs={'class':'form-control'}),
            'patient_birth':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'patient_blood':forms.Select(attrs={'class':'form-control'}),
            'patient_status':forms.Select(attrs={'class':'form-control'}),
            'patient_married':forms.Select(attrs={'class':'form-control'}),
            'patient_gender':forms.Select(attrs={'class':'form-control'}),
            'patient_acceptance':forms.Select(attrs={'class':'form-control'}),
            'patient_discription':forms.Textarea(attrs={'class':'form-control'}),
            'check_in_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'diseases':forms.TextInput(attrs={'class':'form-control'}),
            'patient_room':forms.Select(attrs={'class':'form-control'}),
        }
class DiseasesForm(forms.ModelForm):
    class Meta:
        model = PatientHistory
        fields = '__all__'
        widgets = {
            'patient_fullname':forms.Select(attrs={'class':'form-control'}),
            'patient': forms.Select(attrs={'class':'form-control' }),
            'patient_acceptance':forms.Select(attrs={'class':'form-control'}),
            'check_in_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'disease': forms.TextInput(attrs={'class':'form-control'}),
            'retsept': forms.TextInput(attrs={'class':'form-control'}),
            'patient_status':forms.Select(attrs={'class':'form-control'}),
            'payments':forms.Select(attrs={'class':'form-control'}),
            'total_status':forms.Select(attrs={'class':'form-control'}),
            'payment_price': forms.NumberInput(attrs={'class':'form-control'}),
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorCreate
        fields = '__all__'  

class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = AddExpense
        fields = '__all__'   
        widgets = {
            'expense_head':forms.TextInput(attrs={'class':'form-control','placeholder':'Ta\'mirlash uskunalari'}),
            'select_category':forms.Select(attrs={'class':'form-control wide'}),
            'amount':forms.TextInput(attrs={'class':'form-control', 'placeholder':'$5,600'}),
            'expense_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'discreption':forms.Textarea(attrs={'class':'form-control  message','placeholder':'Qisqa tavsif yozing'}),
            'card_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'**** **** **** 5648'}),
            'select_bank':forms.Select(attrs={'class':'form-control'}),
            }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['patient_fullname', 'payment_price', 'payment_choice', 'amount_paid', 'payment_term']
        widgets = {
            'patient_fullname': forms.Select(attrs={'class':'form-control' }),
            'payment_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'5,600,000'}),
            'payments':forms.Select(attrs={'class':'form-control','placeholder':'Naqd pul'}),
            'amount_paid':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'1,000,000'}),
            'payment_term':forms.TextInput(attrs={'class':'form-control', 'placeholder':'3kun'}),
        }

class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'
        widgets = {
            'room_number':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'101'}),
            'room_status':forms.Select(attrs={'class':'form-control','placeholder':'Comfort xona(vip)'}),
            'booked':forms.Select(attrs={'class':'form-control','placeholder':'Comfort xona(vip)'}),
            'yotoq_soni':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'101'}),
        }
#calendarrr
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields ='__all__'
        widgets = {
            'title':forms.TextInput(attrs={'type': 'text', 'class':'form-control'}),
            'description':forms.Textarea(attrs={'type': 'text', 'class':'form-control'}),
            'start_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control '}),
            'start_time':forms.TimeInput(attrs={'type': 'time', 'class':'form-control '}),
            'end_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control '}),
            'end_time':forms.TimeInput(attrs={'type': 'time', 'class':'form-control '}),
            'doctor':forms.Select(attrs={'class':'form-control'}),

        }