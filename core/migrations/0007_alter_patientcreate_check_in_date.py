# Generated by Django 4.2.7 on 2023-12-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_patientcreate_check_in_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientcreate',
            name='check_in_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
