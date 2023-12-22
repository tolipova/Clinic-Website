from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name="home"),
    path('patient-list/',patient_list, name="patient_list"),
    path('patient-profile/',  patient_profile, name="patient_profile"),
    path('add-patient/', add_patient, name="add_patient"),
    path('all-doctors/', all_doctors, name="all_doctors"),
    path('doctor-profile/', doctor_profile, name="doctor_profile"),
    path('add-doctor/', add_doctor, name="add_doctor"),
    path('appointment', appointment, name="appointment"),
    path('operation/', operation, name="operation"),
    path('emergency-form/', emergency_form, name="emergency_form"),
    path('emergency-list/', emergency_list, name="emergency_list"),
    path('reports/', reports, name="reports"),
    path('accounts/', accounts, name="accounts"),
    path('expense-list/', expense_list, name="expense_list"),
    path('add-expense/', add_expense, name="add_expense"),
    path('patient/<uuid:pk>/', patient_profile, name='patient_profile'),
    path('patient/<uuid:pk>/edit/', patient_edit, name='patient_edit'),
    path('patient/<uuid:pk>/delete/', patient_delete, name="patient_delete"),
    path('diseases/<uuid:pk>/', diseases, name='diseases'),
    path('doctor/<uuid:pk>/', doctor_profile, name='doctor_profile'),
    path('doctor/<uuid:pk>/edit/', doctor_edit, name='doctor_edit'),
    path('tulov/', tulov, name="tulov"),
    path('rooms/', rooms_list, name="rooms_list"),
    path('add_room/',add_room, name="add_room"),
    path('room/<int:room_id>/edit/', room_edit, name='room_edit'),
    path('discount_calculation/', discount_calculation, name="discount_calculation")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)