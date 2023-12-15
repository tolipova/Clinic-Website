from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.db.models import Q
from datetime import date, timedelta
# Create your views here.
def home(request):
    today = date.today()
    patients_today = PatientCreate.objects.filter(check_in_date=today).count()
    patients_previous_days = PatientCreate.objects.filter(check_in_date__lt=today).exclude(check_in_date=today).count()
    total_patients = PatientCreate.objects.count()
    total_doctor = DoctorCreate.objects.count()  # bemorlarning sonini hisoblash uchun funksiya
    total_rooms = Rooms.objects.count()
    total_operations = Operation.objects.count()
    doctors = DoctorCreate.objects.all()
    patient = PatientHistory.objects.all()
    expense = AddExpense.objects.all()
    
    context = {
        'total_patients': total_patients,
        'doctors': doctors,
        'patient': patient,
        'expense': expense,
        'total_doctor':total_doctor,
        'total_rooms':total_rooms,
        'total_operations':total_operations,
        'patients_today':patients_today,
        'patients_previous_days':patients_previous_days
    }
    return render(request, 'index.html', context)

def patient_list(request):
    search_query = request.GET.get('q')
    patient = PatientCreate.objects.all()

    if search_query:
        patient = patient.filter(
            Q(patient_fullname__icontains=search_query) |
            Q(patient_key__icontains=search_query) |
            Q(patient_phone__icontains=search_query) |
            Q(patient_id__icontains=search_query)  
        )
    paginator = Paginator(patient, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query 
    }
    return render(request, 'patient/patient-list.html', context)

    paginator = Paginator(patient, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query  # Passing the search query back to the template
    }
    return render(request, 'patient/patient-list.html', context)

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

def doctor_profile(request, pk):
    doctor = get_object_or_404(DoctorCreate, pk=pk)
    context = {
        'doctor':doctor
    }
    return render(request,'doctor/doctor-Profile.html', context )
def doctor_edit(request, pk):
    doctor = get_object_or_404(DoctorCreate, pk=pk)
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_profile', pk=pk)  # Redirect to patient detail page after successful update
    else:
        form = DoctorForm(instance=doctor)
    
    return render(request, 'doctor/doctor_edit.html', {'form': form, 'doctor': doctor})
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
    expense = AddExpense.objects.all()
    paginator = Paginator(expense, 1)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'expense/expense-list.html', context)
def add_expense(request):
    form = AddExpenseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddExpenseForm()    
    return render(request, 'expense/add-expense.html',{'form':form})

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

def tulov(request):
    return render(request, 'tulov.html')
    






