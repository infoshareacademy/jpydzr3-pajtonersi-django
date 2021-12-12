from django.test import TestCase, Client
from django.urls import reverse_lazy
from http import HTTPStatus


class UserCreateTestCase(TestCase):
    def test_create_view(self):
        client = Client()
        response = client.get(reverse_lazy('patient_create'))
        expected = HTTPStatus.OK
        self.assertEqual(expected, response.status_code)
