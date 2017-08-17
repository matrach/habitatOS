from django.contrib import admin
from habitat.health.models import Urine


@admin.register(Urine)
class UrineAdmin(admin.ModelAdmin):
    pass
