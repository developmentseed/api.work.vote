from django.contrib import admin

from .models import Jurisdiction, State, SurveyEmail
from .email_survey import dispatch_email


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

def send_email(modeladmin, request, queryset):
    for email_req in queryset:
        obj_list = email_req.jurisdictions.all()
        jurisdiction_list = []
        for jurisdiction in obj_list:
            jurisdiction_list.append([jurisdiction.name, jurisdiction.pk])
            print(jurisdiction_list)
        else:
            print("EMPTY")
        response_code = dispatch_email(jurisdiction_list, email_req.recipients)
        if response_code == 200:
            queryset.update(send_email=True)
send_email.short_description = "Send e-mail"

class SurveyEmailAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'send_email', 'recipients'
    )
    actions = [send_email]
    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return [] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return ['send_email']

admin.site.register(State, StateAdmin)
admin.site.register(SurveyEmail, SurveyEmailAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
