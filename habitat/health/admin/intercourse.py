from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Intercourse


@admin.register(Intercourse)
class IntercourseAdmin(HabitatAdmin):
    pass
