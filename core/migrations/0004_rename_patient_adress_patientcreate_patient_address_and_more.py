# Generated by Django 4.2.7 on 2023-12-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_doctorcreate_patientcreate_delete_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientcreate',
            old_name='patient_adress',
            new_name='patient_address',
        ),
        migrations.RenameField(
            model_name='patientcreate',
            old_name='patient_male',
            new_name='patient_gender',
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_address',
            field=models.CharField(default=1, max_length=255, verbose_name='Doktorning manzili'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_age',
            field=models.IntegerField(default=1, verbose_name='Doktorning yoshi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_birth',
            field=models.CharField(default=1, max_length=255, verbose_name="Tug'ilgan kun/oy/yil"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_blood',
            field=models.CharField(choices=[('α va β', 'birinchi (0)'), ('A va β', 'ikkinchi (A)'), ('α va B', 'uchinchi (B)'), ('A va B', 'toʻrtinchi (AB)')], default=1, max_length=255, verbose_name='Qon gruxi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_discription',
            field=models.TextField(default=1, verbose_name="Qo'shimcha ma'lumot"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_image',
            field=models.ImageField(default=1, upload_to='user_info/', verbose_name='doktor rasmi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_phone',
            field=models.IntegerField(default=1, verbose_name='Doktorning telefon raqami'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='doctor_skills',
            field=models.CharField(choices=[('Farmatsevt', 'Farmatsevt'), ('Ginekolog', 'Ginekolog'), ('Audiolog', 'Audiolog')], default=1, max_length=255, verbose_name='Doktor qobiliyati'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorcreate',
            name='email_address',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
        migrations.AddField(
            model_name='patientcreate',
            name='patient_discription',
            field=models.TextField(default=1, verbose_name="Qo'shimcha ma'lumot"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientcreate',
            name='patient_married',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried')], default=1, max_length=255, verbose_name='Turmush holati'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctorcreate',
            name='doctor_status',
            field=models.CharField(choices=[('Tibbiyot mutaxassisi', 'Tibbiyot mutaxassisi'), ('Ginekolog', 'Ginekolog'), ('Jismoniy terapiya', 'Jismoniy terapiya'), ('Audiologiya', 'Audiologiya'), ('Kordiolog', 'Kordiolog'), ('Hamshira', 'Hamshira')], max_length=255, verbose_name='Shifokorning lavozimi'),
        ),
        migrations.AlterField(
            model_name='patientcreate',
            name='patient_blood',
            field=models.CharField(choices=[('α va β', 'birinchi (0)'), ('A va β', 'ikkinchi (A)'), ('α va B', 'uchinchi (B)'), ('A va B', 'toʻrtinchi (AB)')], max_length=255, verbose_name='Qon gruxi'),
        ),
    ]
