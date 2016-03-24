from django.contrib import admin

from .models import Application, Survey


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
    readonly_fields = ('created_at', 'age_range', 'languages', 'familiarity_w_technology', 'city',
                       'jurisdiction', 'county')

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'export_url': '/contacts/applications_export',
            'export_caption': 'Download Applications',
            'show_export_button': True
        }

        return super(ApplicationAdmin, self).changelist_view(request, extra_context)


class SurveyAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'age_range',
        'languages'
    )

    readonly_fields = ('created_at', 'age_range', 'languages', 'familiarity_w_technology')

    list_filter = ('age_range',)

    ordering = ['-created_at']

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'export_url': '/contacts/surveys_export',
            'export_caption': 'Download Surveys',
            'show_export_button': True
        }

        return super(SurveyAdmin, self).changelist_view(request, extra_context)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Survey, SurveyAdmin)
