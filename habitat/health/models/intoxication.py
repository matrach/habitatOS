from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Intoxication(HabitatModel, MissionDateTime, ReporterAstronaut):
    """
    Medicines
    Ethanol
    """
    pass
