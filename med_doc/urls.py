from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from med_doc.views import create_visit


urlpatterns = [
    path('create_visit', create_visit, name='create_visit')
]
