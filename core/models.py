from django.db import models
import uuid
import random
from django.urls import reverse
from django.utils import timezone
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
    ('Turmush qurgan','Turmush qurgan'),
    ('Turmush qurmagan','Turmush qurmagan')
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
operatsion_type = (
    ("Ko'krak jarrohligi" , "Ko'krak jarrohligi"),
    ("Ko'z jarrohligi", "Ko'z jarrohligi")

)
operatsion_serves = (
    ("Ko'krak jarrohligi" , "Ko'krak jarrohligi"),
    ("Ko'z jarrohligi", "Ko'z jarrohligi")

)
select_category = (
    ("Kommunal xizmatlar uchun to'lov","Kommunal xizmatlar uchun to'lov"),
    ("Ta'mirlash uskunalari uchun to'lov","Ta'mirlash uskunalari uchun to'lov"),
    ("Kerakli retseptlar uchun to'lov","Kerakli retseptlar uchun to'lov")
)
bank = (
    ("NBU Bank","NBU Bank"),
    ("Hamkor Bank","Hamkor Bank"),
    ("Humo Xalq Banki","Humo Xalq Banki")
)
booked_room = (
     ("Bo'sh xona","Bo'sh xona"),
     ("Band qilingan","Band qilingan")
)
class DoctorCreate(models.Model):
    doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor_fullname = models.CharField(verbose_name='Doctorning ism familiyasi', max_length=255)
    profile_image = models.ImageField(upload_to='user_info/', verbose_name="doktor profil rasmi")
    muqova_image = models.ImageField(upload_to='user_info/', verbose_name="doktor muqova rasmi")
    doctor_phone = models.IntegerField(verbose_name='Doktorning telefon raqami')
    doctor_address = models.CharField(verbose_name='Doktorning manzili', max_length=255)
    doctor_age = models.IntegerField(verbose_name='Doktorning yoshi')
    doctor_blood = models.CharField(verbose_name='Qon gruxi',choices=qon_guruxlari, max_length=255)
    doctor_status = models.CharField(verbose_name='Shifokorning lavozimi', choices=doctor_lavozimi, max_length=255)
    email_address = models.EmailField(max_length=70,blank=True,unique=True)
    doctor_birth = models.DateField(auto_now=False)
    doctor_skills = models.CharField(choices=doctor_skills, verbose_name="Doktor qobiliyati",max_length=255)
    doctor_discription = models.TextField(verbose_name="Qo'shimcha ma'lumot")
    doctor_university = models.TextField(verbose_name="doctor tamomlagan university")
    work_time = models.TimeField(auto_now=False)
    
    def get_absolute_url(self):
            return reverse('doctor_profile', kwargs={'pk': self.pk})

    def get_edit_url(self):
            return reverse('doctor_edit', kwargs={'pk': self.pk})
    def __str__(self):
        return self.doctor_fullname
     
class Rooms(models.Model):
    room_number = models.IntegerField(verbose_name="xona raqami", null=True, blank=True) 
    room_status = models.CharField(max_length=255, choices=qabul_holati, verbose_name="xona turi")
    yotoq_soni = models.IntegerField(verbose_name='Yotoqlar soni')
    booked = models.CharField(max_length=255, choices=booked_room, verbose_name="xona holati" )
    
    def __str__(self):
        return str(self.room_number) 
      
class PatientCreate(models.Model):
    
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    patient_fullname = models.CharField(verbose_name='Bemorning ism familiyasi', max_length=255,null=True)
    patient_phone = models.IntegerField(verbose_name='Bemorning telefon raqami')
    patient_address = models.CharField(verbose_name='Bemorning manzili', max_length=255,null=True)
    patient_birth = models.DateField(auto_now=False)
    patient_age = models.IntegerField(verbose_name='Bemorning yoshi',null=True)
    patient_blood = models.CharField(verbose_name='Qon gruxi',choices=qon_guruxlari, max_length=255,null=True)
    patient_status = models.CharField(choices=qabul_holati, verbose_name='Qabul holati', max_length=255,null=True)
    patient_married = models.CharField(choices=turmush_holati, verbose_name='Turmush holati', max_length=255,null=True)
    patient_gender = models.CharField(verbose_name='Jinsi', choices=jinsi, max_length=255,null=True)
    patient_acceptance = models.ForeignKey(DoctorCreate, on_delete=models.CASCADE, null=True)
    patient_discription = models.TextField(verbose_name="Qo'shimcha ma'lumot", null=True)
    check_in_date = models.DateField(auto_now =False )
    diseases = models.CharField(max_length=255, verbose_name="kasallik nommi", null=True)
    patient_room = models.ForeignKey(Rooms, on_delete=models.CASCADE,null=True )
    patient_key = models.CharField(verbose_name='Patient Key', max_length=9, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.patient_key:
            self.patient_key = self.generate_unique_key()
        super().save(*args, **kwargs)

    def generate_unique_key(self):
        key = ''.join(str(random.randint(0, 9)) for _ in range(9))
        while PatientCreate.objects.filter(patient_key=key).exists():
            key = ''.join(str(random.randint(0, 9)) for _ in range(9))
        return key
    
    def get_absolute_url(self):
            return reverse('patient_profile', kwargs={'pk': self.pk})

    def get_edit_url(self):
            return reverse('patient_edit', kwargs={'pk': self.pk})
    #O'RGANISHGAAAAAAAAAAAA
    @staticmethod
    def kunlik_bemor_count():
        bugun = timezone.now().date()
        count = PatientCreate.objects.filter(check_in_date=bugun).count()
        return count
    def __str__(self):
        return self.patient_fullname
    
class Operation(models.Model):
    patient_fullname = models.ForeignKey(PatientCreate, verbose_name='Bemorning ism familiyasi',on_delete=models.CASCADE )
    operatsion_date = models.DateField(auto_now=False )
    operatsion_time = models.TimeField(auto_now=False )
    select_operatsion_type = models.CharField(choices=operatsion_type, verbose_name="operatsiya turini tanlang",max_length=255)
    select_operatsion_serves =  models.CharField(choices=operatsion_serves, verbose_name="operatsiya xizmat turini tanlang",max_length=255)
    operatsion_price = models.IntegerField(verbose_name="operatsiya narxi")
    operatsion_discount = models.IntegerField(verbose_name="chegirma summasi")
    total_grand = models.IntegerField(verbose_name="umumiy grand narxi")
    paid_amount = models.IntegerField(verbose_name="to'langan miqdor")
    comment = models.TextField(verbose_name="Izoh qoldiring")
    
    def __str__(self):
        return self.patient_fullname
    
class AddExpense(models.Model):
    expense_head = models.CharField(max_length=255, verbose_name="harajat nomi")
    select_category = models.CharField(choices=select_category, max_length=255)
    amount = models.CharField(verbose_name="miqdori", max_length=25)
    expense_date = models.DateTimeField(auto_now=False )
    discreption = models.TextField(verbose_name="tavsilot kiriting")
    card_number = models.IntegerField(verbose_name="**** **** **** 5648")
    select_bank = models.CharField(max_length=255, verbose_name="kerakli bankni tanlang",choices=bank)

    def __str__(self):
        return self.expense_head
    


class PatientHistory(models.Model):
    patient_fullname = models.ForeignKey(PatientCreate, verbose_name='Bemorning ism familiyasi', on_delete=models.CASCADE, related_name='patient_fullnames')
    check_in_date = models.DateField(verbose_name="ruyxatdan o'tgan sanasi")
    patient_acceptance = models.ForeignKey(DoctorCreate, on_delete=models.CASCADE, related_name='patient_acceptances')
    disease = models.CharField(max_length=255, verbose_name="kasallik turi")
    retsept = models.TextField(verbose_name="kerakli dorilar")
    patient_status = models.CharField(choices=qabul_holati, max_length=255)
    
    PAYMENT_CHOICES = [
        ('Naqd pul', 'Naqd pul'),
        ('Plastik karta', 'Plastik karta'),
        ('Sug\'urta', 'Sug\'urta'),
     
    ]
    payments = models.CharField(choices=PAYMENT_CHOICES, max_length=20, verbose_name="to'lov turi")
    payment_price = models.IntegerField(verbose_name="to'lov narxi")
    payment = [
     ("to'lov qilinmagan", "to'lov qilinmagan"),
     ("to'lov qilingan","to'lov qilingan")
    ]
    total_status = models.CharField(choices=payment, max_length=255, verbose_name="to'lov holati")
    def get_absolute_url(self):
        return reverse('patient_profile', kwargs={'pk': self.pk})
    def __str__(self):
        return self.patient_fullname
    
class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="To'lov sanasi")
    patient_fullname = models.ForeignKey(PatientCreate, verbose_name='Bemorning ism familiyasi', on_delete=models.CASCADE, related_name='patient_fullnamee')
    payment_price = models.IntegerField(verbose_name="to'lov narxi")
    PAYMENT_CHOICES = [
        ('Naqd pul', 'Naqd pul'),
        ('Plastik karta', 'Plastik karta'),
        ('Sug\'urta', 'Sug\'urta'),
     
    ]
    payment_choice =  models.CharField(choices=PAYMENT_CHOICES, max_length=20, verbose_name="to'lov turi")
    amount_paid = models.IntegerField(verbose_name="to'langan summa")
    payment_term = models.CharField(max_length=255, verbose_name="to'lov muddati")
#O'RGANISHGAAAAAAAAAAAA
    @property
    def calculate_debt(self):
        return self.payment_price - self.amount_paid
    
    def __str__(self):
        return self.payment_choice


# calendar
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(auto_now=False)
    start_time = models.TimeField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    doctor =  models.ForeignKey(DoctorCreate, on_delete=models.CASCADE, verbose_name="doctorlar")
    def __str__(self):
        return self.title