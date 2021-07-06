from django.core.exceptions import ValidationError
from django.apps import apps as django_apps
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_consent.field_mixins import IdentityFieldsMixin, ReviewFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import PersonalFieldsMixin, VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import IDENTITY_TYPE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_identifier.subject_identifier import SubjectIdentifier
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from edc_constants.choices import GENDER
from edc_utils import age

from ..choices import MARITAL_STATUS, LIVE_WITH


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(
    ConsentModelMixin, SiteModelMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    NonUniqueSubjectIdentifierModelMixin,
    IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
    CitizenFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    subject_screening_model = 'training_subject.subjectscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        max_length=50)

    consent_datetime = models.DateTimeField(
        verbose_name='Consent date and time',
        default=get_utcnow,
        help_text='Date and time of consent.')

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=IDENTITY_TYPE)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=10,
        null=True,
        blank=False)

    status = models.CharField(
        verbose_name='What is the subject marital status?',
        choices=MARITAL_STATUS, max_length=10)

    no_of_partners = models.PositiveSmallIntegerField(
        verbose_name='No. of partners?'
    )

    live_with = models.CharField(
        verbose_name='Who do you currently live with?',
        choices=LIVE_WITH, max_length=25
    )

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier}'

    def natural_key(self):
        return self.subject_identifier

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        screening_cls = django_apps.get_model('training_subject.subjectscreening')
        try:
            screening_obj = screening_cls.objects.get(
                screening_identifier=self.screening_identifier)
        except screening_cls.DoesNotExist:
            raise ValidationError(f'Missing subject screening object for participant{self.subject_identifier}')
        else:
            # screening_obj.age_in_years = age(self.dob, get_utcnow())
            screening_obj.save()
        self.subject_type = 'subject'
        self.version = '1'

    class Meta(ConsentModelMixin.Meta):
        app_label = 'training_subject'
        verbose_name = 'Subject Consent'
        unique_together = (
            ('subject_identifier', 'screening_identifier'),
            ('first_name', 'dob', 'initials'))
