from django.test import TestCase, Client
from django.urls import reverse_lazy
from users.test_samples import variable_samples


class UserCreateTestCase(TestCase):
    def test_create_view(self):
        client = Client()
        response = client.get(reverse_lazy('patient_create'))
        expected = variable_samples.user_create_get
        self.assertEqual(expected, response.rendered_content)
