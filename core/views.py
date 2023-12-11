from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    patient_add = PatientCreate.objects.all()
    doctors = DoctorCreate.objects.all()
    patient = PatientHistory.objects.all()
    context = {
        'patient_add':patient_add,
        'doctors':doctors,
        'patient':patient
    }
    return render(request,'index.html', context )

def patient_list(request):
    patient = PatientCreate.objects.all()
    paginator = Paginator(patient, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request,'patient/patient-list.html',context)

def patient_profile(request, pk):
    patient = get_object_or_404(PatientCreate, pk=pk)
    patient_view = get_object_or_404(PatientHistory, pk=pk)
    return render(request, 'patient/Patient-Profile.html', {'patient': patient, 'patient_view':patient_view})
    #return render(request,'patient/Patient-Profile.html' )

def patient_edit(request, pk):
    patient = get_object_or_404(PatientCreate, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', pk=pk)  # Redirect to patient detail page after successful update
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'patient/patient_edit.html', {'form': form, 'patient': patient})

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
    form = DoctorCreateForm(request.POST ,request.FILES)
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
    form = OperationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('xato')
    else:
        form = OperationForm() 
    return render(request,'operation.html',{'form':form})

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

def diseases(request):
    form = DiseasesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('xato')
    else:
        form = DiseasesForm() 
    return render(request, 'patient/diseases.html',{'form':form} )


    






