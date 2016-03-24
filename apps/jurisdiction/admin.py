from django.contrib import admin

from .models import Jurisdiction, State


class JurisdictionAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'state',
        'website',
        'telephone',
        'email',
        'city',
    )

    list_filter = ('state', 'city',)

    search_fields = ('name', 'state__name', 'telephone',)

    ordering = ['name']

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'export_url': '/jurisdictions/emails',
            'export_caption': 'Download Jurisdiction Emails',
            'show_export_button': True
        }

        return super(JurisdictionAdmin, self).changelist_view(request, extra_context)


class StateAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'alpha',
        'pollworker_website',
    )

    search_fields = ('name', 'alpha',)

    ordering = ['name']


admin.site.register(State, StateAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
