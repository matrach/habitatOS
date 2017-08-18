from django.contrib import admin
from habitat.health.models import Weight


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    date_hierarchy = 'datetime'
    list_display = ['datetime', 'astronaut', 'weight', 'BMI', 'body_fat', 'lean_body_mass', 'body_water', 'muscle_mass', 'bone_mass', 'daily_caloric_intake', 'visceral_fat']
    list_filter = ['astronaut', 'BMI']
