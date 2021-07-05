from django.contrib import admin
from ..models import SubjectConsent
from ..main_admin import training_subject_admin
from ..forms import SubjectConsentForm


@admin.register(SubjectConsent, site=training_subject_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    form = SubjectConsentForm
    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'consent_datetime',
                'first_name',
                'last_name',
                'initials',
                'gender',
                'dob',
                'is_dob_estimated',
                'identity',
                'confirm_identity',
                'identity_type',

            ),
        }),
    )

    search_fields = ('subject_identifier',)

    radio_fields = {
        'gender': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'identity_type': admin.VERTICAL
    }

    readonly_fields = ('subject_identifier',)
