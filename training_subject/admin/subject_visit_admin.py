from django.contrib import admin
from ..models import SubjectVisit
from ..main_admin import training_subject_admin
from ..forms import SubjectVisitForm


@admin.register(SubjectVisit, site=training_subject_admin)
class SubjectVisitAdmin(admin.ModelAdmin):
    form = SubjectVisitForm
