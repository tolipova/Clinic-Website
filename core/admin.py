from django.contrib import admin
from .models import *
# Register your models here.
class Patient(admin.ModelAdmin):
    list_display = ('patient_key', 'patient_fullname',)
    list_filter = ('patient_key',)
    
admin.site.register(PatientCreate,Patient)
admin.site.register(DoctorCreate)
admin.site.register(Rooms)
admin.site.register(Operation)
admin.site.register(Event)
admin.site.register(Payment)