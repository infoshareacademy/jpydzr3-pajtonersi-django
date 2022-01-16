"""medyczna_placowka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import profile

from django.contrib import admin
from django.contrib.auth.views import LoginView

from users import views
from django.urls import path, include
from users.views import Login, login_success, ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('login_success/', login_success, name='login_success'),
    path('profile/<slug:user__username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<slug:user__username>/profile_edycja.html', ProfileUpdateView.as_view(), name='profile_edycja'),
]
