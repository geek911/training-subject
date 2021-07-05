from django.contrib import admin
from ..models import EducationQuestionnaire
from ..main_admin import training_subject_admin
from ..forms import EducationQuestionnaireForm


@admin.register(EducationQuestionnaire, site=training_subject_admin)
class EducationQuestionnaireAdmin(admin.ModelAdmin):
    form = EducationQuestionnaireForm
