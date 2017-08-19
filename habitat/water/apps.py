from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WaterConfig(AppConfig):
    name = 'habitat.water'
    label = 'water'
    verbose_name = _('Water Report')
