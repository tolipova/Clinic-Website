from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    patient_add = PatientCreate.objects.all()
    doctors = DoctorCreate.objects.all()
    context = {
        'patient_add':patient_add,
        'doctors':doctors
    }
    return render(request,'index.html', context )

def patient_list(request):
    patient = PatientCreate.objects.all()
    paginator = Paginator(patient, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request,'patient/patient-list.html',context)

def patient_profile(request):
    return render(request,'patient/Patient-Profile.html' )

def add_patient(request):
    form = PatientCreateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientCreateForm()    
    return render(request,'patient/add-new-patient.html',{'form':form} )

def all_doctors(request):
    doctors = DoctorCreate.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'doctor/all-doctors.html',context )

def doctor_profile(request):
    doctors = DoctorCreate.objects.all()
    context = {
        'doctors':doctors
    }
    return render(request,'doctor/doctor-Profile.html', context )

def add_doctor(request):
    form = DoctorCreateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DoctorCreateForm()    
    return render(request,'doctor/add-new-doctor.html',{'form':form} )

def appointment(request):
    return render(request,'doctor/appointment.html' )
def operation(request):
    return render(request,'operation.html' )
def emergency_form(request):
    return render(request,'emergency/emergency-form.html' )
def emergency_list(request):
    return render(request,'emergency/emergency-list.html' )
def reports(request):
    return render(request, 'reports.html')
def accounts(request):
    return render(request, 'accounts.html')
def expense_list(request):
    return render(request, 'expense/expense-list.html')
def add_expense(request):
    return render(request, 'expense/add-expense.html')








    






