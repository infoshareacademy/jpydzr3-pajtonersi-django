from django.test import TestCase, Client
from django.urls import reverse_lazy
from http import HTTPStatus
from users.models import Patient


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
        self.assertEqual(patient_query.count(), 1)
        self.assertEqual(HTTPStatus.FOUND, response.status_code)

    def test_database_save_no_data(self):
        parameters = {

        }
        response = self.client.post(reverse_lazy('patient_create'), data=parameters)
        patient_query = Patient.objects.all()
        self.assertEqual(patient_query.count(), 0)
        self.assertEqual(HTTPStatus.OK, response.status_code)
