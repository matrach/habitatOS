from django.contrib import admin
from django.apps import apps
from django.core.exceptions import AppRegistryNotReady

try:
    all_models = apps.get_models()
    registered_models = admin.site._registry

    for model in all_models:
        if model not in registered_models:
            try:
                admin.site.register(model, model.Admin)
            except AttributeError:
                admin.site.register(model)

except AppRegistryNotReady:
    pass
