from django import forms
from edc_form_validators import FormValidatorMixin
from training_validations.form_validators import EducationQuestionnaireFormValidator

from ..models import EducationQuestionnaire


class EducationQuestionnaireForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = EducationQuestionnaireFormValidator

    class Meta:
        model = EducationQuestionnaire
        fields = '__all__'
