from django.test import TestCase
from patient.models import Patient
from django.shortcuts import get_object_or_404

# Create your tests here.

class PatientTestCase(TestCase):

    def setUp(self):
        Patient.objects.create(firstname="Themba",lastname="Tshoane",province="Gauteng",region="Pretoria",location="Pretoria West")
        Patient.objects.create(firstname="Leka",lastname="Tshwane",province="Gauteng",region="Pretoria",location="Mamelodi")

    def test_add_patient(self):

        
        themba = Patient.objects.get(firstname='Themba')
        leka = Patient.objects.get(firstname='Leka')

        self.assertEqual(themba.firstname,"Themba")
        self.assertEqual(themba.lastname,"Tshoane")
        self.assertEqual(themba.province,"Gauteng")
        self.assertEqual(themba.region,"Pretoria")
        self.assertEqual(themba.location,"Pretoria West")

        self.assertEqual(leka.firstname,"Leka")
        self.assertEqual(leka.lastname,"Tshwane")
        self.assertEqual(leka.province,"Gauteng")
        self.assertEqual(leka.region,"Pretoria")
        self.assertEqual(leka.location,"Mamelodi")

    def test_detail(self):
        patient = get_object_or_404(Patient,pk=1)
        self.assertEqual(patient.firstname,"Themba")





    
