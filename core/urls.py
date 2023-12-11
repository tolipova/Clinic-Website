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
    path('patient/<uuid:pk>/view/', patient_history_view, name='history_view')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)