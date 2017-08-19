from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Intoxication


@admin.register(Intoxication)
class IntoxicationAdmin(HabitatAdmin):
    """
    Medicines
    Ethanol
    """
    pass
