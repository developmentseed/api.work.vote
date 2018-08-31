from django.contrib import admin

from .models import Jurisdiction, State, SurveyEmail
from mailman.mailer import MailSurvey


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
    count_success = 0
    count_resend = 0
    tot_reqs = 0
    for email_req in queryset:
        tot_reqs +=1
        # Only send e-mail once
        if email_req.send_email == False:
            obj_list = email_req.jurisdiction.all()
            jurisdiction_list = []
            for jurisdiction in obj_list:
                jurisdiction_list.append([jurisdiction.name, jurisdiction.pk])
            jurisdiction_list.sort(key=lambda x: x[0])
            # send email
            mail = MailSurvey(jurisdiction_list, email_req.recipients)
            status = mail.send()
            if status == 'OK':
                queryset.update(send_email=True)
                count_success+=1
        else:
            count_resend +=1
        
    message=""
    if count_success > 0:
        message += "{} out of {} e-mails were successfully sent.".format(count_success, tot_reqs)
    if count_resend > 0:
        message += '{} out of {} e-mails have already been sent to their recipient. No action has been taken. To force a re-send, set "Sent E-mail?" to False'
    modeladmin.message_user(request,  message)

send_email.short_description = "Send e-mail"

def mark_unsent(modeladmin, request, queryset):
    queryset.update(send_email=False)
mark_unsent.short_description = "Mark e-mail as not sent"

class SurveyEmailAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'send_email', 'recipients'
    )
    actions = [send_email, mark_unsent]
    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return [] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return ['send_email']

admin.site.register(State, StateAdmin)
admin.site.register(SurveyEmail, SurveyEmailAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
