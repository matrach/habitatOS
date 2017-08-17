from django.contrib import admin
from habitat.health.models import Weight


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'astronaut', 'weight', 'BMI', 'body_fat', 'lean_body_mass', 'body_water', 'muscle_mass', 'bone_mass', 'daily_caloric_intake', 'visceral_fat']
    list_filter = ['astronaut', 'BMI']
    date_hierarchy = 'datetime'
