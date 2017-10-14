from datetime import datetime
from datetime import timezone
from django.conf import settings
from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from habitat._common.admin import HabitatAdmin
from habitat._common.admin import HabitatTabularInline
from habitat.communication.models import Email
from habitat.communication.models import Attachment


class InboxFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Show')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'inbox'

    def lookups(self, request, model_admin):
        return [
            ('received', _('Received')),
            ('sent', _('Sent')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'sent':
            return queryset.filter(sender=request.user)

        if self.value() == 'received':
            return queryset.exclude(sender=request.user)


class AttachmentInline(HabitatTabularInline):
    model = Attachment
    extra = 3


@admin.register(Email)
class EmailAdmin(HabitatAdmin):
    list_display = ['date', 'time', 'sender', 'subject']
    list_filter = [InboxFilter, 'to']
    list_display_links = ['subject']
    search_fields = ['sender__username', 'subject', 'body']
    ordering = ['-modified']
    exclude = ['sender', 'date', 'time']
    raw_id_fields = ['to']
    autocomplete_lookup_fields = {'m2m': ['to']}
    inlines = [AttachmentInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        delay = now() - settings.HABITATOS['DELAY']
        received = queryset.filter(to=request.user, modified__lt=delay)
        sent = queryset.filter(sender=request.user)
        return sent | received

    def save_model(self, request, obj, form, change):
        obj.sender = request.user
        super().save_model(request, obj, form, change)
