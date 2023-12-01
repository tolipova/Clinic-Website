from django.db import models
import uuid
# Create your models here.
qon_guruxlari =(
    ("α va β", "birinchi (0)"),
    ("A va β", "ikkinchi (A)"),
    ("α va B","uchinchi (B)"),
    ("A va B","toʻrtinchi (AB)")
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
turmush_holati = (
    ('Married','Married'),
    ('Unmarried','Unmarried')
)
doctor_lavozimi = (
    ('Tibbiyot mutaxassisi', 'Tibbiyot mutaxassisi'),
    ('Ginekolog','Ginekolog'),
    ('Jismoniy terapiya','Jismoniy terapiya'),
    ('Audiologiya','Audiologiya'),
    ('Kordiolog', 'Kordiolog'),
    ('Hamshira','Hamshira')
)
doctor_skills = (
    ('Farmatsevt','Farmatsevt'),
    ('Ginekolog','Ginekolog'),
    ('Audiolog','Audiolog')
)
class DoctorCreate(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_fullname = models.CharField(verbose_name='Doctorning ism familiyasi', max_length=255)
    doctor_image = models.ImageField(upload_to='user_info/', verbose_name="doktor rasmi")
    doctor_phone = models.IntegerField(verbose_name='Doktorning telefon raqami')
    doctor_address = models.CharField(verbose_name='Doktorning manzili', max_length=255)
    doctor_age = models.IntegerField(verbose_name='Doktorning yoshi')
    doctor_blood = models.CharField(verbose_name='Qon gruxi',choices=qon_guruxlari, max_length=255)
    doctor_status = models.CharField(verbose_name='Shifokorning lavozimi', choices=doctor_lavozimi, max_length=255)
    email_address = models.EmailField(max_length=70,blank=True,unique=True)
    doctor_birth = models.CharField(max_length=255, verbose_name="Tug'ilgan kun/oy/yil")
    doctor_skills = models.CharField(choices=doctor_skills, verbose_name="Doktor qobiliyati",max_length=255)
    doctor_discription = models.TextField(verbose_name="Qo'shimcha ma'lumot")
    
    
    def __str__(self):
        return self.doctor_fullname
    
class PatientCreate(models.Model):
    
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_fullname = models.CharField(verbose_name='Bemorning ism familiyasi', max_length=255)
    patient_phone = models.IntegerField(verbose_name='Bemorning telefon raqami')
    patient_address = models.CharField(verbose_name='Bemorning manzili', max_length=255)
    patient_age = models.IntegerField(verbose_name='Bemorning yoshi')
    patient_blood = models.CharField(verbose_name='Qon gruxi',choices=qon_guruxlari, max_length=255)
    patient_status = models.CharField(choices=qabul_holati, verbose_name='Qabul holati', max_length=255)
    patient_married = models.CharField(choices=turmush_holati, verbose_name='Turmush holati', max_length=255)
    patient_gender = models.CharField(verbose_name='Jinsi', choices=jinsi, max_length=255)
    patient_acceptance = models.ForeignKey(DoctorCreate, on_delete=models.CASCADE)
    patient_discription = models.TextField(verbose_name="Qo'shimcha ma'lumot")
    
    
    def __str__(self):
        return self.patient_fullname