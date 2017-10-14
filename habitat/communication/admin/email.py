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


class AttachmentReadOnlyInline(AttachmentInline):
    can_delete = False
    readonly_fields = ['file']
    max_num = 0
    min_num = 0
    extra = 0

    def has_add_permission(self, request):
        return False


@admin.register(Email)
class EmailAdmin(HabitatAdmin):
    actions = None
    list_display = ['date', 'time', 'sender', 'subject']
    list_filter = [InboxFilter, 'to']
    list_display_links = ['subject']
    search_fields = ['sender__username', 'to__username', 'subject', 'body']
    ordering = ['-modified']
    exclude = ['sender', 'date', 'time']
    raw_id_fields = ['to']
    autocomplete_lookup_fields = {'m2m': ['to']}
    readonly_fields = ['id']
    inlines = [AttachmentInline]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = [AttachmentReadOnlyInline]
        extra_context = extra_context or {}
        extra_context['readonly'] = True
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        extra_context['show_delete_link'] = False
        self.Media.js += [
            'communication/js/email-reply-button.js',
            'communication/js/email-hide-save.js',
        ]
        return super().change_view(request, object_id, form_url, extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['sender', 'to', 'subject', 'body']
        else:
            return self.readonly_fields

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
        return super().save_model(request, obj, form, change)

    class Media:
        js = []
        css = {'all': [
            'communication/css/hide-id-field.css',
        ]}
