from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_identifier.simple_identifier import SimpleUniqueIdentifier
from edc_search.model_mixins import SearchSlugModelMixin, SearchSlugManager
from edc_constants.choices import GENDER, YES_NO
from edc_utils import get_utcnow
from django_countries.fields import CountryField
from ..utils import is_eligible
from django.db import models

questions = [
    'Eligibility Identifier',
    'Report Date and Time',
    'Subject country of citizenship?',
    'Subject gender',
    'Subject age',
    'Did subject provide marriage proof?',
    'Is the subject literate',
    'If not literate, does the subject have a literate witness?',
    'If minor, does the subject have a guardian?',
    'Subject spouse citizenship if married'
]


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class ScreeningIdentifier(SimpleUniqueIdentifier):
    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'


class SubjectScreening(NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin, SearchSlugModelMixin, BaseUuidModel, ):
    screening_identifier = models.CharField(
        verbose_name=questions[0],
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name=questions[1],
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')

    subject_citizenship = CountryField(
        verbose_name=questions[2],
    )

    subject_spouse_citizenship = CountryField(
        verbose_name=questions[9]
    )

    gender = models.CharField(
        verbose_name=questions[3],
        max_length=10,
        choices=GENDER
    )

    age = models.PositiveSmallIntegerField(
        verbose_name=questions[4]
    )

    marriage_proof = models.CharField(
        verbose_name=questions[5],
        max_length=10,
        choices=YES_NO
    )

    is_subject_literate = models.CharField(
        verbose_name=questions[6],
        max_length=10,
        choices=YES_NO
    )

    is_literate_witness_available = models.CharField(
        verbose_name=questions[7],
        max_length=10,
        choices=YES_NO
    )

    is_guardian_available = models.CharField(
        verbose_name=questions[8],
        max_length=10,
        choices=YES_NO
    )

    is_eligible = models.BooleanField(editable=False)

    history = HistoricalRecords()

    objects = SubjectScreeningManager()

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('screening_identifier')
        return fields

    def __str__(self):
        return self.screening_identifier

    def natural_key(self):
        return self.screening_identifier

    def save(self, *args, **kwargs):
        self.is_eligible = is_eligible(
            citizen=self.subject_citizenship,
            spouse_citizenship=self.subject_spouse_citizenship,
            age=self.age,
            marriage_proof=self.marriage_proof,
            is_literate=self.is_subject_literate,
            is_witness_literate=self.is_literate_witness_available,
            guardian_available=self.is_guardian_available
        )
        if not self.screening_identifier:
            self.screening_identifier = ScreeningIdentifier().identifier
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'training_subject'
        verbose_name = 'Eligibility Confirmation'
        verbose_name_plural = 'Eligibility Confirmation'
