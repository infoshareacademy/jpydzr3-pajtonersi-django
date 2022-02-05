from django import forms

from users.models import Patient


class PatientCreate(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'country',
            'city'
        )
