from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import Patient


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login_success')


def login_success(request):
    return render(request, "users/login_success.html", {})


class PatientCreateView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'patient_create.html'
