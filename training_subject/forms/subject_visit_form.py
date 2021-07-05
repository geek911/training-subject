from django import forms
from ..models import SubjectVisit


class SubjectVisitForm(forms.ModelForm):
    class Meta:
        model = SubjectVisit
        fields = '__all__'
