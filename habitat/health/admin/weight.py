from django.contrib import admin
from habitat._common.admin import HabitatAdmin
from habitat.health.models import Weight


@admin.register(Weight)
class WeightAdmin(HabitatAdmin):
    list_display = ['date', 'time', 'reporter', 'weight', 'BMI', 'body_fat', 'lean_body_mass', 'body_water', 'muscle_mass', 'bone_mass', 'daily_caloric_intake', 'visceral_fat']
    list_filter = ['reporter', 'BMI']
