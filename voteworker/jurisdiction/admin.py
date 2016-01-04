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


admin.site.register(State)
admin.site.register(Jurisdiction, JurisdictionAdmin)
