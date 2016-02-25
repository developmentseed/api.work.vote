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


class StateAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'alpha',
        'state_id',
        'pollworker_website',
    )

    search_fields = ('name', 'alpha', 'state_id',)

    ordering = ['name']


admin.site.register(State, StateAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
