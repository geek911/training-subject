from django.contrib import admin
from edc_action_item.admin.modeladmin_mixins import ModelAdminMixin
from edc_model_admin import ModelAdminBasicMixin
from simple_history.admin import SimpleHistoryAdmin

from ..models import CommunityQuestionnaire
from ..main_admin import training_subject_admin
from ..forms import CommunityQuestionnaireForm


@admin.register(CommunityQuestionnaire, site=training_subject_admin)
class CommunityQuestionnaireAdmin(
    ModelAdminBasicMixin,
    ModelAdminMixin,
    SimpleHistoryAdmin,
    admin.ModelAdmin):
    form = CommunityQuestionnaireForm

    radio_fields = {
        'active_community': admin.VERTICAL,
        'did_you_vote': admin.VERTICAL,
        'problem_in_neighborhood': admin.VERTICAL
    }

    filter_horizontal = ('neighborhood',)
