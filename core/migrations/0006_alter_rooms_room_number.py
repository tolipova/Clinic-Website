# Generated by Django 4.2.7 on 2023-12-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rooms_patientlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_number',
            field=models.IntegerField(blank=True, default=1, verbose_name='xona raqami'),
            preserve_default=False,
        ),
    ]