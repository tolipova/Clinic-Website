# Generated by Django 4.2.7 on 2023-12-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_patienthistory_payment_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='payment_price',
            field=models.IntegerField(verbose_name="to'lov narxi"),
        ),
    ]