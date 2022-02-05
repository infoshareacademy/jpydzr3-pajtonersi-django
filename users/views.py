from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView


from users.models import Profile


class Login(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self) -> str:
        return reverse('profile', kwargs={'user__username': self.request.user.username})


def login_success(request):
    return render(request, "users/login_success.html", {})


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
