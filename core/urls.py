from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(),name=' login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-done/',PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complate'),
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
    path('discount_calculation/', discount_calculation, name="discount_calculation"),
    #calendarr
    path('events/', EventView.as_view(), name='event'),
    path('delete_event/<int:event_id>/', EventView.as_view(), name='delete_event'),
    # path('events/', event_list, name='event_list'),
    # path('events/create/', create_event, name='create_event'),
    # path('events/<int:event_id>/edit/',edit_event, name='edit_event'),
    # path('events/<int:event_id>/delete/', delete_event, name='delete_event'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)