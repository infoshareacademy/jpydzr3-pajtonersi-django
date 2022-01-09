from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import ugettext as _

USER = get_user_model()


class Receptionist(USER):
    class Meta:
        verbose_name = _('recepcjonista')


class Patient(USER):
    pass


class Doctor(USER):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    phone = models.CharField('numer telefonu', max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super(Profile, self).save(*args, **kwargs)







