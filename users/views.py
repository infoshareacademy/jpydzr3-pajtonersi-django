from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse

from users.models import Patient, Doctor, Profile


class Login(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self) -> str:
        return reverse('profile', kwargs={'user__username': self.request.user.username})

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

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        profile = Profile.objects.create(
            user=self.object
        )
        profile.save()
        return HttpResponseRedirect(self.get_success_url())


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
