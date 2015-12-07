from django.contrib import admin

from .models import Jurisdiction, State


class JurisdictionAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'state',
        'website',
        'telephone',
        'email',
    )

    list_filter = ('state',)

    search_fields = ('name', 'state__name', 'telephone',)


admin.site.register(State)
admin.site.register(Jurisdiction, JurisdictionAdmin)
