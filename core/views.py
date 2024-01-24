from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.db.models import Q
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.
@login_required
def home(request):
    today = date.today()
    year_added =  PatientCreate.yillk_count()
    monthly_added = PatientCreate.oylik_bemor_count()
    weekly_added = PatientCreate.haftalik_bemor_count()
    daily_added = PatientCreate.kunlik_bemor_count()
    patients_today = PatientCreate.objects.filter(check_in_date=today).count()
    patients_previous_days = PatientCreate.objects.filter(check_in_date__lt=today).exclude(check_in_date=today).count()
    total_patients = PatientCreate.objects.count()
    total_doctor = DoctorCreate.objects.count()  # bemorlarning sonini hisoblash uchun funksiya
    total_rooms = Rooms.objects.count()
    total_operations = Operation.objects.count()
    doctors = DoctorCreate.objects.all()
    patient = PatientHistory.objects.all()
    expense = AddExpense.objects.all()

    search_query = request.GET.get('q')
    patients_search = PatientCreate.objects.all()
    doctors_search = DoctorCreate.objects.all()
    expense_search = AddExpense.objects.all()
    operations_search = Operation.objects.all()
    rooms_search = Rooms.objects.all()
    if search_query:
        patients_search = patients_search.filter(
            Q(patient_fullname__icontains=search_query) |
            Q(patient_key__icontains=search_query) |
            Q(patient_id__icontains=search_query) )
    elif search_query:
        doctors_search = doctors_search.filter(
            Q(doctor_fullname__icontains=search_query) |
            Q(doctor_id__icontains=search_query) |
            Q(doctor_status__icontains=search_query) )
    elif search_query:
        expense_search = expense_search.filter(
            Q(expense_head__icontains=search_query) )
    elif search_query:
        operations_search = operations_search.filter(
            Q(select_operatsion_type__icontains=search_query) )
    elif search_query:
        rooms_search = rooms_search.filter(
            Q(room_number__icontains=search_query) 
            )

    context = {
        'year_added':year_added,
        'monthly_added':monthly_added,
        'weekly_added':weekly_added,
        'daily_added':daily_added,
        'total_patients': total_patients,
        'doctors': doctors,
        'patient': patient,
        'expense': expense,
        'total_doctor':total_doctor,
        'total_rooms':total_rooms,
        'total_operations':total_operations,
        'patients_today':patients_today,
        'patients_previous_days':patients_previous_days,
        'search_query':search_query
    }
    return render(request, 'index.html', context)
class PatientView(View):
    def get(self, request):
        search_query = request.GET.get('q')
        patients = PatientCreate.objects.all()

        if search_query:
            patients = patients.filter(
                Q(patient_fullname__icontains=search_query) |
                Q(patient_key__icontains=search_query) |
                Q(patient_phone__icontains=search_query) |
                Q(patient_id__icontains=search_query)
            )

        paginator = Paginator(patients, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'page_obj': page_obj,
            'search_query': search_query,
            'form': PatientCreateForm(),  # Include an instance of the patient form for the template
        }
        return render(request, 'patient/patient-list.html', context)

    def post(self, request):
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change 'home' to your desired redirect path

        search_query = request.GET.get('q')
        patients = PatientCreate.objects.all()

        if search_query:
            patients = patients.filter(
                Q(patient_fullname__icontains=search_query) |
                Q(patient_key__icontains=search_query) |
                Q(patient_phone__icontains=search_query) |
                Q(patient_id__icontains=search_query)
            )
        paginator = Paginator(patients, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'search_query': search_query,
            'form': form,  # Pass the form with errors back to the template
        }
        return render(request, 'patient/patient-list.html', context)

    def diseases(self, request, pk):
        form = DiseasesForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                print('Error: Form is invalid')
        else:
            form = DiseasesForm()

        return render(request, 'patient/diseases.html', {'form': form})

# def patient_list(request):
#     search_query = request.GET.get('q')
#     patient = PatientCreate.objects.all()

#     if search_query:
#         patient = patient.filter(
#             Q(patient_fullname__icontains=search_query) |
#             Q(patient_key__icontains=search_query) |
#             Q(patient_phone__icontains=search_query) |
#             Q(patient_id__icontains=search_query)  
#         )
#     paginator = Paginator(patient, 25)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#         'search_query': search_query 
#     }
#     return render(request, 'patient/patient-list.html', context)


def patient_profile(request, pk):
    patient = get_object_or_404(PatientCreate, pk=pk)
    patient_view = PatientHistory.objects.filter(patient_fullname=patient)
    return render(request, 'patient/Patient-Profile.html', {'patient': patient, 'patient_view':patient_view})
    #return render(request,'patient/Patient-Profile.html' )

def patient_delete(request, pk):
    patient = PatientCreate.objects.get(pk=pk)
    patient.delete()
    return redirect('patient_list')

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
        form = DoctorCreateForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_profile', pk=pk)  # Redirect to patient detail page after successful update
    else:
        form = DoctorCreateForm(instance=doctor)
    
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

class OperationView(View):
    def get(self,request):
        operations = Operation.objects.all()
        form = OperationForm()
        return render(request, 'operations_list.html', {'operations':operations, 'form':form})

    def post(self, request):
        form = OperationForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = OperationForm()    
        return render(request, 'operations_list.html',{'form':form})

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

def diseases(request, pk):
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




def add_room(request):
    form = RoomsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('xato')
    else:
        form = RoomsForm() 
    return render(request, 'rooms/add_new_room.html', {'form':form})

def rooms_list(request):
    search_query = request.GET.get('q')
    rooms = Rooms.objects.all()

    if search_query:
        rooms = rooms.filter(
            Q(room_number__icontains=search_query)
        )
    
    paginator = Paginator(rooms, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'rooms': rooms
    }
    return render(request, 'rooms/rooms_list.html', context)

def room_edit(request, room_id):
    room = get_object_or_404(Rooms, id=room_id)
    
    if request.method == 'POST':
        form = RoomsForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', room_id=room.id)
    else:
        form = RoomsForm(instance=room)
    
    return render(request, 'rooms/room_edit.html', {'form': form, 'room': room})
#calendarrr

# def event_list(request):
#     events = Event.objects.all()
#     return render(request, 'event/event_list.html', {'events': events})

# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#     else:
#         form = EventForm()
#     return render(request, 'event/create_event.html', {'form': form})

# def edit_event(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     if request.method == 'POST':
#         form = EventForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#     else:
#         form = EventForm(instance=event)
#     return render(request, 'event/edit_event.html', {'form': form})

# def delete_event(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     if request.method == 'POST':
#         event.delete()
#         return JsonResponse({'success': True, 'message': 'Event deleted successfully'})
#     return render(request, 'event/delete_event.html', {'event': event})
class TulovView(View):
    def get(self,request):
        tulov = Payment.objects.all()
        form = PaymentForm()
        return render(request, 'tulov.html', {'tulov':tulov, 'form':form})
    
    def post(self, request):
        form = PaymentForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PaymentForm()    
        return render(request, 'tulov.html',{'form':form})
class EventView(View):
    def get(self, request):
        events = Event.objects.all()
        form = EventForm()
        return render(request, 'doctor/event_list.html', {'events': events, 'form': form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
        events = Event.objects.all()
        return render(request, 'doctor/event_list.html', {'events': events, 'form': form})

    def put(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event')
        events = Event.objects.all()
        return render(request, 'doctor/event_list.html', {'events': events, 'form': form})

    def delete(self, request, event_id):

        event = get_object_or_404(Event, pk=event_id)
        if request.method == 'POST':
            try:
                event.delete()
                return JsonResponse({'success': True, 'message': 'Event deleted successfully'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        events = Event.objects.all()

        return render(request, 'doctor/event_list.html', {'event': event})
