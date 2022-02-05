from django.test import TestCase, Client
from django.urls import reverse_lazy
from http import HTTPStatus
from users.models import Patient, Profile, Doctor


class UserCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_view(self):
        response = self.client.get(reverse_lazy('patient_create'))
        expected = HTTPStatus.OK
        self.assertEqual(expected, response.status_code)

    def test_database_save(self):
        parameters = {
            'first_name': 'Jarek',
            'last_name': 'Majka',
            'pesel': '123456789101',
            'tel_no': '123456789',
            'password': '111111',
            'username': 'admin123',
        }
        response = self.client.post(reverse_lazy('patient_create'), data=parameters)
        patient_query = Patient.objects.filter(first_name=parameters['first_name'])
        profile_query = Profile.objects.filter(user__username=parameters['username'])
        self.assertEqual(patient_query.count(), 1)
        # self.assertEqual(profile_query.count(), 1)
        assert profile_query.count() == 1
        self.assertEqual(HTTPStatus.FOUND, response.status_code)

    def test_database_save_no_data(self):
        parameters = {

        }
        response = self.client.post(reverse_lazy('patient_create'), data=parameters)
        patient_query = Patient.objects.all()
        self.assertEqual(patient_query.count(), 0)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_create_doctor(self):
        specialty = next((specialty[0] for specialty in Doctor.SPECIALTY_CHOICES if specialty[1] == "Ogólny"), None)
        parameters = {
            'first_name': 'Jarek',
            'last_name': 'Majka',
            'pesel': '123456789101',
            'tel_no': '123456789',
            'password': '111111',
            'username': 'admin123',
            'specialty': specialty,
        }

        response = self.client.post(reverse_lazy('doctor_create'), data=parameters)
        doctor_query = Doctor.objects.filter(first_name=parameters['first_name'])
        self.assertEqual(doctor_query.count(), 1)
        self.assertEqual(HTTPStatus.FOUND, response.status_code)

    def test_create_doctor_no_data(self):
        parameters = {}

        response = self.client.post(reverse_lazy('doctor_create'), data=parameters)
        doctor_query = Doctor.objects.all()
        self.assertEqual(doctor_query.count(), 0)
        self.assertEqual(HTTPStatus.OK, response.status_code)