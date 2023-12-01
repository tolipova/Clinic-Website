from django.db import models
import uuid
# Create your models here.
qon_gruxlari =(
    ("A", "A"),
    ("B", "B")
)
qabul_holati = (
    ('Vip', 'Vip'),
    ('Oddiy', 'Oddiy'),
    ('Budjet',' Budjet')
)

jinsi = (
    ('Ayol', 'Ayol'),
    ('Erkak', 'Erkak')
)
doctor_lavozimi = (
    ('Hamshira', 'Hamshira'),
    ('Kordiolog', 'Kordiolog')
)
class DoctorCreate(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_fullname = models.CharField(verbose_name='Doctorning ism familiyasi', max_length=255)
    doctor_status = models.CharField(verbose_name='Shifokorning lavozimi', choices=doctor_lavozimi, max_length=255)
    def __str__(self):
        return self.doctor_fullname
    
class PatientCreate(models.Model):
    
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_fullname = models.CharField(verbose_name='Bemorning ism familiyasi', max_length=255)
    patient_phone = models.IntegerField(verbose_name='Bemorning telefon raqami')
    patient_adress = models.CharField(verbose_name='Bemorning manzili', max_length=255)
    patient_age = models.IntegerField(verbose_name='Bemorning yoshi')
    patient_blood = models.CharField(verbose_name='Qon gruxi',choices=qon_gruxlari, max_length=255)
    patient_status = models.CharField(choices=qabul_holati, verbose_name='Qabul holati', max_length=255)
    patient_male = models.CharField(verbose_name='Jinsi', choices=jinsi, max_length=255)
    patient_acceptance = models.ForeignKey(DoctorCreate, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patient_fullname