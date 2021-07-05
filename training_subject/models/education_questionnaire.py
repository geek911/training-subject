from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_constants.choices import YES_NO
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_search.model_mixins import SearchSlugManager
# from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin

from .subject_visit import SubjectVisit
from ..choices import TYPE_OF_WORK, PREVIOUS_JOB_TYPE_WORK, SALARY_RANGE


class EducationQuestionnaireManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class EducationQuestionnaire(CrfModelMixin,
                             RequiresConsentFieldsModelMixin,
                             SubjectScheduleCrfModelMixin,
                             UpdatesCrfMetadataModelMixin,
                             SiteModelMixin,
                             ReferenceModelMixin,
                             BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=models.DO_NOTHING)

    working_status = models.CharField(
        verbose_name='Are you currently working?',
        choices=YES_NO,
        max_length=5
    )

    type_of_work = models.CharField(
        verbose_name='In you job what type of work do you do?',
        choices=TYPE_OF_WORK,
        max_length=50
    )

    previous_work = models.CharField(
        verbose_name='Describe the work that you do or did in your most recent job. If you have more than one profession, choose the one you spend the most time doing.',
        choices=PREVIOUS_JOB_TYPE_WORK,
        max_length=50
    )

    salary_range = models.CharField(
        verbose_name='In the past month, how much money did you earn from work you did or received in payment?',
        choices=SALARY_RANGE,
        max_length=50
    )

    def __str__(self):
        return f'{self.subject_identifier}'

    def natural_key(self):
        return self.subject_identifier

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'training_subject'
        verbose_name = 'Education Questionnaire'
