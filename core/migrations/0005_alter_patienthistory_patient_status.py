# Generated by Django 4.2.7 on 2023-12-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_patienthistory_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='patient_status',
            field=models.CharField(choices=[('Vip', 'Vip'), ('Oddiy', 'Oddiy'), ('Budjet', ' Budjet')], max_length=255),
        ),
    ]
