from django.contrib import admin
from ..models import SubjectScreening
from ..main_admin import training_subject_admin
from ..forms import SubjectScreeningForm


@admin.register(SubjectScreening, site=training_subject_admin)
class SubjectScreeningAdmin(admin.ModelAdmin):
    form = SubjectScreeningForm
    fields = [
        'report_datetime',
        'subject_citizenship',
        'subject_spouse_citizenship',
        'gender',
        'age',
        'marriage_proof',
        'is_subject_literate',
        'is_literate_witness_available',
        'is_guardian_available',
    ]
