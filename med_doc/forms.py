from django import forms

from med_doc.models import Visit


class BootstrapDateTimePickerInput(forms.DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context


class VisitForm(forms.ModelForm):
    visit_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )

    class Meta:
        model = Visit
        fields = ['doctor', 'patient', 'created_by', 'additional_info']

        # TODO: patient not visible if visit created by himself
