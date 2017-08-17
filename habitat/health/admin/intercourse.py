from django.contrib import admin
from habitat.health.models import Intercourse


@admin.register(Intercourse)
class IntercourseAdmin(admin.ModelAdmin):
    pass
