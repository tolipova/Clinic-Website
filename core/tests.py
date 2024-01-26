# test.py
from django.test import TestCase, TransactionTestCase
from .models import PatientCreate, DoctorCreate, Rooms
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone
import random

class PatientModelTest(TransactionTestCase):
    def doctor_create(self, suffix=''):
        return DoctorCreate.objects.create(
            doctor_fullname=f'Test duxtr {suffix}',
            profile_image=f'path/to/your/image_{suffix}.jpg',
            muqova_image=f'path/to/your/muqova_image_{suffix}.jpg',
            doctor_phone=f'1234567890{suffix}',
            doctor_address=f'Test Address{suffix}',
            doctor_age=30,
            doctor_blood='A+',
            doctor_status=f'Doxtr Status {suffix}',  
            
            email_address=f'duxtr{suffix}@maiil.com',
            doctor_birth='1990-01-01',
            doctor_skills=f'Doctor Skills {suffix}', 
            doctor_discription=f'Test Description {suffix}',
            doctor_university=f'Doctor univesitet {suffix}',  
            work_time=f'12:00:00',
    )
        
    def setUp(self):
        doctor = self.doctor_create()
        room = Rooms.objects.create(room_number='101', room_status='oddiy', yotoq_soni=5, booked='ochiq')
        
            
        PatientCreate.objects.create( 
                patient_fullname='Test kasal', patient_phone='1234567890', patient_address='Test manzil', patient_birth='1990-01-01',
                patient_age=30, patient_blood='A+', patient_status='oddiy', patient_married='oilali',patient_gender='erkak',
                patient_acceptance=doctor, patient_discription='Test qushimcha',check_in_date='2024-01-24',diseases='shamollash',
                patient_room=room,  
            )
        
    
    def run_tests(self, num_tests):
        for i in range(num_tests):
            uzgaruvchi = f'_{i}'
            doctor = self.doctor_create(uzgaruvchi)
            
            room = Rooms.objects.create(room_number=f'101_{i}', room_status='oddiy', yotoq_soni=5, booked='ochiq')
            patient = PatientCreate.objects.create(
                    patient_fullname=f'Test kasal {uzgaruvchi}',
                    patient_phone=f'1234567890{uzgaruvchi}',
                    patient_address=f'Test manzil {uzgaruvchi}',
                    patient_birth='1990-01-01',
                    patient_age=30,
                    patient_blood='A+',
                    patient_status='oddiy',
                    patient_married='oilali',
                    patient_gender='erkak',
                    patient_acceptance=doctor,
                    patient_discription='Test qushimcha',
                    check_in_date='2024-01-24',
                    diseases=f'shamollash {uzgaruvchi}',
                    patient_room=room,
            )
            self.assertIsNotNone(patient.patient_key)
            url = patient.get_absolute_url()
            self.assertEqual(url, reverse('patient_profile', kwargs={'pk':patient.pk}))
            url = patient.get_edit_url()
            self.assertEqual(url, reverse('patient_edit', kwargs={'pk':patient.pk}))
    def test_run_tests(self):
        self.run_tests(50)        
        
# class PatientModelTest(TestCase):
#     def setUp(self):
#         doctor = DoctorCreate.objects.create(
#             doctor_fullname='Test duxtr',
#             profile_image='path/to/your/image.jpg',
#             muqova_image='path/to/your/muqova_image.jpg',
#             doctor_phone='1234567890',
#             doctor_address='Test Address',
#             doctor_age=30,
#             doctor_blood='A+',
#             doctor_status='Doxtr Status',  
#             email_address='duxtr@maiil.com',
#             doctor_birth='1990-01-01',
#             doctor_skills='Doctor Skills', 
#             doctor_discription='Test Description',
#             doctor_university='Doctor univesitet',  
#             work_time='12:00:00',
#         )
#         room = Rooms.objects.create(room_number='101', room_status='oddiy', yotoq_soni=5, booked='ochiq')

#         PatientCreate.objects.create(
#             patient_fullname='Test kasal',
#             patient_phone='1234567890',
#             patient_address='Test manzil',
#             patient_birth='1990-01-01',
#             patient_age=30,
#             patient_blood='A+',
#             patient_status='oddiy',
#             patient_married='oilali',
#             patient_gender='erkak',
#             patient_acceptance=doctor,
#             patient_discription='Test qushimcha',
#             check_in_date='2024-01-24',
#             diseases='shamollash',
#             patient_room=room,
#         )

#     def test_patient_key_generation(self):
#         patient = PatientCreate.objects.get(patient_fullname='Test kasal')
#         self.assertIsNotNone(patient.patient_key)

#     def test_get_absolute_url(self):
#         patient = PatientCreate.objects.get(patient_fullname='Test kasal')
#         url = patient.get_absolute_url()
#         self.assertEqual(url, reverse('patient_profile', kwargs={'pk': patient.pk}))

#     def test_get_edit_url(self):
#         patient = PatientCreate.objects.get(patient_fullname='Test kasal')
#         url = patient.get_edit_url()
#         self.assertEqual(url, reverse('patient_edit', kwargs={'pk': patient.pk}))
