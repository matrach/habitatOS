from django.contrib import admin
from habitat.health.models import Intoxication


@admin.register(Intoxication)
class IntoxicationAdmin(admin.ModelAdmin):
    """
    Medicines
    Ethanol
    """
    pass
