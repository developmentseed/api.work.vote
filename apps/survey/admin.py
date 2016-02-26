from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'jurisdiction',
        'city',
        'age_range',
        'languages',
        'familiarity_w_technology'
    )

    list_filter = ('age_range', 'jurisdiction__state')

    search_fields = ('city', 'county', 'jurisdiction__name')

    ordering = ['-created_at']


admin.site.register(Application, ApplicationAdmin)
