from django.db.models.base import Model
from django.forms import ModelForm, fields


from med_doc.models import Visit


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ['visit_date', 'doctor', 'patient', 'created_by', 'additional_info']

        # TODO: patient not visible if visit created by himself
