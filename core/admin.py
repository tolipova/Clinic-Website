from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PatientCreate)
admin.site.register(DoctorCreate)
admin.site.register(Rooms)
admin.site.register(Operation)
