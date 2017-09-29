from django.conf import settings
from django.utils.module_loading import import_string
from .models import *


def get_timezone():
    timezone = settings.HABITATOS['TIME_ZONE']
    cls = import_string(timezone)
    return cls
