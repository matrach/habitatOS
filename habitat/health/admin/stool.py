from django.contrib import admin
from habitat.health.models import Stool


@admin.register(Stool)
class StoolAdmin(admin.ModelAdmin):
    pass
