from django.contrib import admin
from django.apps import apps

# Autodiscover and register all admin
# Models should have Admin class inside

for model in apps.get_models():
    if model not in admin.site._registry:
        try:

            # If model.Admin has property hidden, that we do not load this
            # Default action is to include everything

            if not getattr(model.Admin, 'hidden', False):
                admin.site.register(model, model.Admin)

        except AttributeError:
            pass
