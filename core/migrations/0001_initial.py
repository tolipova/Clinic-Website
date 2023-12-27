# Generated by Django 4.2.7 on 2023-12-27 06:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_head', models.CharField(max_length=255, verbose_name='harajat nomi')),
                ('select_category', models.CharField(choices=[("Kommunal xizmatlar uchun to'lov", "Kommunal xizmatlar uchun to'lov"), ("Ta'mirlash uskunalari uchun to'lov", "Ta'mirlash uskunalari uchun to'lov"), ("Kerakli retseptlar uchun to'lov", "Kerakli retseptlar uchun to'lov")], max_length=255)),
                ('amount', models.CharField(max_length=25, verbose_name='miqdori')),
                ('expense_date', models.DateTimeField()),
                ('discreption', models.TextField(verbose_name='tavsilot kiriting')),
                ('card_number', models.IntegerField(verbose_name='**** **** **** 5648')),
                ('select_bank', models.CharField(choices=[('NBU Bank', 'NBU Bank'), ('Hamkor Bank', 'Hamkor Bank'), ('Humo Xalq Banki', 'Humo Xalq Banki')], max_length=255, verbose_name='kerakli bankni tanlang')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorCreate',
            fields=[
                ('doctor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doctor_fullname', models.CharField(max_length=255, verbose_name='Doctorning ism familiyasi')),
                ('profile_image', models.ImageField(upload_to='user_info/', verbose_name='doktor profil rasmi')),
                ('muqova_image', models.ImageField(upload_to='user_info/', verbose_name='doktor muqova rasmi')),
                ('doctor_phone', models.IntegerField(verbose_name='Doktorning telefon raqami')),
                ('doctor_address', models.CharField(max_length=255, verbose_name='Doktorning manzili')),
                ('doctor_age', models.IntegerField(verbose_name='Doktorning yoshi')),
                ('doctor_blood', models.CharField(choices=[('α va β', 'birinchi (0)'), ('A va β', 'ikkinchi (A)'), ('α va B', 'uchinchi (B)'), ('A va B', 'toʻrtinchi (AB)')], max_length=255, verbose_name='Qon gruxi')),
                ('doctor_status', models.CharField(choices=[('Tibbiyot mutaxassisi', 'Tibbiyot mutaxassisi'), ('Ginekolog', 'Ginekolog'), ('Jismoniy terapiya', 'Jismoniy terapiya'), ('Audiologiya', 'Audiologiya'), ('Kordiolog', 'Kordiolog'), ('Hamshira', 'Hamshira')], max_length=255, verbose_name='Shifokorning lavozimi')),
                ('email_address', models.EmailField(blank=True, max_length=70, unique=True)),
                ('doctor_birth', models.DateField()),
                ('doctor_skills', models.CharField(choices=[('Farmatsevt', 'Farmatsevt'), ('Ginekolog', 'Ginekolog'), ('Audiolog', 'Audiolog')], max_length=255, verbose_name='Doktor qobiliyati')),
                ('doctor_discription', models.TextField(verbose_name="Qo'shimcha ma'lumot")),
                ('doctor_university', models.TextField(verbose_name='doctor tamomlagan university')),
                ('work_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientCreate',
            fields=[
                ('patient_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_fullname', models.CharField(max_length=255, null=True, verbose_name='Bemorning ism familiyasi')),
                ('patient_phone', models.IntegerField(verbose_name='Bemorning telefon raqami')),
                ('patient_address', models.CharField(max_length=255, null=True, verbose_name='Bemorning manzili')),
                ('patient_birth', models.DateField()),
                ('patient_age', models.IntegerField(null=True, verbose_name='Bemorning yoshi')),
                ('patient_blood', models.CharField(choices=[('α va β', 'birinchi (0)'), ('A va β', 'ikkinchi (A)'), ('α va B', 'uchinchi (B)'), ('A va B', 'toʻrtinchi (AB)')], max_length=255, null=True, verbose_name='Qon gruxi')),
                ('patient_status', models.CharField(choices=[('Vip', 'Vip'), ('Oddiy', 'Oddiy'), ('Budjet', ' Budjet')], max_length=255, null=True, verbose_name='Qabul holati')),
                ('patient_married', models.CharField(choices=[('Turmush qurgan', 'Turmush qurgan'), ('Turmush qurmagan', 'Turmush qurmagan')], max_length=255, null=True, verbose_name='Turmush holati')),
                ('patient_gender', models.CharField(choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')], max_length=255, null=True, verbose_name='Jinsi')),
                ('patient_discription', models.TextField(null=True, verbose_name="Qo'shimcha ma'lumot")),
                ('check_in_date', models.DateField()),
                ('diseases', models.CharField(max_length=255, null=True, verbose_name='kasallik nommi')),
                ('patient_key', models.CharField(editable=False, max_length=9, unique=True, verbose_name='Patient Key')),
                ('patient_acceptance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.doctorcreate')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(blank=True, null=True, verbose_name='xona raqami')),
                ('room_status', models.CharField(choices=[('Vip', 'Vip'), ('Oddiy', 'Oddiy'), ('Budjet', ' Budjet')], max_length=255, verbose_name='xona turi')),
                ('yotoq_soni', models.IntegerField(verbose_name='Yotoqlar soni')),
                ('booked', models.CharField(choices=[("Bo'sh xona", "Bo'sh xona"), ('Band qilingan', 'Band qilingan')], max_length=255, verbose_name='xona holati')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name="To'lov sanasi")),
                ('payment_price', models.IntegerField(verbose_name="to'lov narxi")),
                ('payment_choice', models.CharField(choices=[('Naqd pul', 'Naqd pul'), ('Plastik karta', 'Plastik karta'), ("Sug'urta", "Sug'urta")], max_length=20, verbose_name="to'lov turi")),
                ('amount_paid', models.IntegerField(verbose_name="to'langan summa")),
                ('payment_term', models.CharField(max_length=255, verbose_name="to'lov muddati")),
                ('patient_fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_fullnamee', to='core.patientcreate', verbose_name='Bemorning ism familiyasi')),
            ],
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(verbose_name="ruyxatdan o'tgan sanasi")),
                ('disease', models.CharField(max_length=255, verbose_name='kasallik turi')),
                ('retsept', models.TextField(verbose_name='kerakli dorilar')),
                ('patient_status', models.CharField(choices=[('Vip', 'Vip'), ('Oddiy', 'Oddiy'), ('Budjet', ' Budjet')], max_length=255)),
                ('payments', models.CharField(choices=[('Naqd pul', 'Naqd pul'), ('Plastik karta', 'Plastik karta'), ("Sug'urta", "Sug'urta")], max_length=20, verbose_name="to'lov turi")),
                ('payment_price', models.IntegerField(verbose_name="to'lov narxi")),
                ('total_status', models.CharField(choices=[("to'lov qilinmagan", "to'lov qilinmagan"), ("to'lov qilingan", "to'lov qilingan")], max_length=255, verbose_name="to'lov holati")),
                ('patient_acceptance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_acceptances', to='core.doctorcreate')),
                ('patient_fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_fullnames', to='core.patientcreate', verbose_name='Bemorning ism familiyasi')),
            ],
        ),
        migrations.AddField(
            model_name='patientcreate',
            name='patient_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.rooms'),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operatsion_date', models.DateField()),
                ('operatsion_time', models.TimeField()),
                ('select_operatsion_type', models.CharField(choices=[("Ko'krak jarrohligi", "Ko'krak jarrohligi"), ("Ko'z jarrohligi", "Ko'z jarrohligi")], max_length=255, verbose_name='operatsiya turini tanlang')),
                ('select_operatsion_serves', models.CharField(choices=[("Ko'krak jarrohligi", "Ko'krak jarrohligi"), ("Ko'z jarrohligi", "Ko'z jarrohligi")], max_length=255, verbose_name='operatsiya xizmat turini tanlang')),
                ('operatsion_price', models.IntegerField(verbose_name='operatsiya narxi')),
                ('operatsion_discount', models.IntegerField(verbose_name='chegirma summasi')),
                ('total_grand', models.IntegerField(verbose_name='umumiy grand narxi')),
                ('paid_amount', models.IntegerField(verbose_name="to'langan miqdor")),
                ('comment', models.TextField(verbose_name='Izoh qoldiring')),
                ('patient_fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patientcreate', verbose_name='Bemorning ism familiyasi')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctorcreate', verbose_name='doctorlar')),
            ],
        ),
    ]
