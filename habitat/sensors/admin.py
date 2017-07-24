"""
from django.contrib.auth import admin
from django.utils.translation import ugettext_lazy as _


class TempoListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Level')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tempo_all'

    def lookups(self, request, model_admin):
        return [
            ('deadly', _('Deadly')),
            ('critical', _('Critical')),
            ('warning', _('Warning')),
            ('nominal', _('Nominal')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'deadly':
            return queryset.filter(tempo_all__gt=200)

        if self.value() == 'critical':
            return queryset.filter(tempo_all__gt=125, tempo_all__lte=200)

        if self.value() == 'warning':
            return queryset.filter(tempo_all__gte=75, tempo_all__lte=125)

        if self.value() == 'nominal':
            return queryset.filter(tempo_all__gte=25, tempo_all__lt=75)
"""
