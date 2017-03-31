from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sleep(models.Model):
    """
    Sleep 1 (quality)
    Sleep 1 (start)
    Sleep 1 (end)
    Sleep 1 (duration)
    Sleep 1 (location)
    Sleep 2 (start)
    Sleep 2 (end)
    Sleep 2 (duration)
    Sleep 2 (quality)
    Sleep 2 (location)
    Sleep Total (duration)
    """
    pass
