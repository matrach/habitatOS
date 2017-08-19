from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import ReportAstronaut


class Intercourse(HabitatModel, ReportAstronaut):
    """
    sex
    orgasm
    """
