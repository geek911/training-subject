from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_schedule.model_mixins import SubjectScheduleCrfModelMixin
from edc_visit_tracking.model_mixins import CrfModelMixin
from django.db import models
from ..choices import COMM_ACTIVITY, DID_YOU_VOTE, PROBLEM_NEI
from ..list_models import CommunityQuestionnaireList


class EducationQuestionnaireManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class CommunityQuestionnaire(CrfModelMixin,
                             RequiresConsentFieldsModelMixin,
                             SubjectScheduleCrfModelMixin,
                             UpdatesCrfMetadataModelMixin,
                             SiteModelMixin,
                             ReferenceModelMixin,
                             BaseUuidModel
                             ):
    active_community = models.CharField(
        verbose_name='How active are you in community activities such as burial society, Motshelo, Syndicate, PTA, VDC(Village Development Committee), Mophato and development of the community that surrounds you?',
        choices=COMM_ACTIVITY,
        max_length=100
    )

    did_you_vote = models.CharField(
        verbose_name='Did you vote in the last local government election?',
        choices=DID_YOU_VOTE,
        max_length=100
    )

    neighborhood = models.ManyToManyField(
        CommunityQuestionnaireList,
        verbose_name='What are the major problems in this neighborhood',
    )

    problem_in_neighborhood = models.CharField(
        verbose_name='If there is a problem in this neighborhood, do the adults work together in solving it?',
        max_length=30,
        choices=PROBLEM_NEI
    )

    class Meta:
        app_label = 'training_subject'
        verbose_name = 'Community Questionnaire'
