import os

from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


module_name = os.path.basename(os.path.dirname(__file__))


for model in apps.get_app_config(module_name).get_models():
    try:
        try:
            admin.site.register(model, model.Admin)
        except AttributeError:
            admin.site.register(model)
    except AlreadyRegistered:
        pass
