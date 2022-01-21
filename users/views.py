from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView

from users.models import Patient, Doctor

from users.models import Profile


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login_success')


def login_success(request):
    return render(request, "users/login_success.html", {})

  
class PatientCreateView(CreateView):
    model = Patient
    fields = [
        'first_name',
        'last_name',
        'pesel',
        'tel_no',
        'password',
        'username',
    ]
    template_name = 'users/patient_create.html'
    success_url = reverse_lazy('login')


class DoctorCreateView(CreateView):
    model = Doctor
    fields = [
        'first_name',
        'last_name',
        'pesel',
        'tel_no',
        'password',
        'username',
        'specialty',
    ]
    template_name = 'users/patient_create.html'
    success_url = reverse_lazy('login')

    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    slug_url_kwarg = 'user__username'
    slug_field = 'user__username'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        print(obj)
        return obj


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'users/profile_edycja.html'
    fields = '__all__'
    slug_url_kwarg = 'user__username'
    slug_field = 'user__username'
