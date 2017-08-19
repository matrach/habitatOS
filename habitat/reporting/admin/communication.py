from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.reporting.models import Communication


@admin.register(Communication)
class CommunicationAdmin(HabitatAdmin):
    radio_fields = {
        'communication_frequency': admin.HORIZONTAL,
        'communication_desired': admin.HORIZONTAL,
        'personal_preferences': admin.HORIZONTAL,
        'work_preferences': admin.HORIZONTAL,
        'communication_quality': admin.HORIZONTAL,
        'know_already': admin.HORIZONTAL,
        'know_desired': admin.HORIZONTAL,
        'cooperation_quality': admin.HORIZONTAL,
        'trust': admin.HORIZONTAL,
        'team_atmosphere': admin.HORIZONTAL,
        'team_misunderstandings': admin.HORIZONTAL,
    }
