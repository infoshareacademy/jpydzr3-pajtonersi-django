from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.db import models

User = get_user_model()


class PersonalInfoMixin(models.Model):
    pesel = models.CharField(max_length=20, blank=True, null=True)
    tel_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50, help_text="Podaj z numer budynku")
    local_no = models.IntegerField(blank=True, null=True)
    post_code = models.CharField(max_length=20)


class Receptionist(User, PersonalInfoMixin):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('recepcjonista')


class Patient(User, PersonalInfoMixin):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)


class Doctor(User, PersonalInfoMixin):
    SPECIALTY_CHOICES = (
        ('PD', 'Pediata'),
        ('DN', 'Dentysta'),
        ('OG', 'Ogólny'),
    )
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
