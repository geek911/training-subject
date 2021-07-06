from django import forms
from ..models import SubjectScreening
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from training_validations.form_validators import SubjectScreeningFormValidator


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
