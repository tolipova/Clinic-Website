# Generated by Django 4.2.7 on 2023-12-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_doctorcreate_muqova_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorcreate',
            name='muqova_image',
            field=models.ImageField(upload_to='user_info/', verbose_name='doktor muqova rasmi'),
        ),
        migrations.AlterField(
            model_name='doctorcreate',
            name='profile_image',
            field=models.ImageField(upload_to='user_info/', verbose_name='doktor profil rasmi'),
        ),
    ]
