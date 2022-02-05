from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
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

    class Meta:
        verbose_name = _("pacjent")
        verbose_name_plural = _("pacjenci")

class Doctor(User, PersonalInfoMixin):
    SPECIALTY_CHOICES = (
        ('PD', 'Pediata'),
        ('DN', 'Dentysta'),
        ('OG', 'Ogólny'),
    )
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    phone = models.CharField('numer telefonu', max_length=50, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super().save(*args, **kwargs)
