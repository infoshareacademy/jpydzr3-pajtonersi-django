from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext as _

from users.models import Doctor, Patient


User = get_user_model()


class Visit(models.Model):
    visit_date = models.DateTimeField(_("Data wizyty"))
    created_date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT,)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created')
    additional_info = models.TextField(_("Dodatkowe informacje"), blank=True, null=True)
    summary = models.TextField(_('Podsumowanie'), blank=True, null=True)
