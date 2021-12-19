from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView

from users.models import Profile


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login_success')


def login_success(request):
    return render(request, "users/login_success.html", {})


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'




