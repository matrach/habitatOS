from django.contrib import admin
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

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


class HabitatAdmin(admin.ModelAdmin):

    def datetime(self, obj):
        return f'{obj.date} ∇ {obj.time}'

    datetime.allow_tags = False
    datetime.short_description = _('Datetime')
