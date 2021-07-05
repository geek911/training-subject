from django import forms
from ..models import CommunityQuestionnaire


class CommunityQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = CommunityQuestionnaire
        fields = '__all__'
