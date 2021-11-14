from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

USER = get_user_model()


class Receptionist(USER):
    class Meta:
        verbose_name = _('recepcjonista')


class Patient(USER):
    pass


class Doctor(USER):
    pass
