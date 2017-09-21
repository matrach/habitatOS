from django.contrib import admin
from django.apps import apps
from import_export.admin import ImportExportModelAdmin

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


class ReporterAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.has_perm('reporting.delete_mood'):
            return queryset
        else:
            return queryset.filter(reporter=request.user)

    def save_model(self, request, obj, form, change):
        obj.reporter = request.user
        super().save_model(request, obj, form, change)


class HabitatAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list_import_export.html'
    change_list_filter_template = 'admin/filter_listing.html'
    ordering = ['-modified']


class HabitatTabularInline(admin.TabularInline):
    pass


class HabitatStackedInline(admin.StackedInline):
    pass
