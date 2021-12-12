from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from django.db import models

User = get_user_model()


class PersonalInfoMixin(models.Model):
    pesel = models.IntegerField(max_length=11)
    tel_no = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50, help_text="Podaj z numer budynku")
    local_no = models.IntegerField(blank=True, null=True)
    post_code = models.CharField(max_length=20)


class Receptionist(User, PersonalInfoMixin):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('recepcjonista')


class Patient(User):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Doctor(User):
    specialty = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
