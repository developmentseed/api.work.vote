from django.contrib import admin

from .models import Survey


class SurveyAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'age_range',
        'languages',
        'familiarity_w_technology'
    )

    list_filter = ('age_range',)

    ordering = [-'created_at']


admin.site.register(Survey, SurveyAdmin)
