from django.contrib import admin
from .models import Jurisdiction, State, SurveyEmail
from mailman.mailer import MailSurvey


class JurisdictionAdmin(admin.ModelAdmin):
    list_display = 'name', 'state', 'website', 'telephone', 'email', 'city'
    list_filter = 'state', 'city'
    fields = (
        ('name', 'state'),
        ('display', 'city'),
        'obtained_at',
        'website', 'application', 'student_website',
        ('telephone', 'email'),
        'office_address', 'mailing_address',
        ('hours_start', 'hours_end'),
        'registration_status', 'voter_registration_url',
        'minimum_age', 'high_school_student',
        'full_day_req',
        'compensation',
        'complete_training', 'post_training_exam',
        'must_have_email',
        'how_obtained',
        'notes', 'further_notes',
        'geometry',
    )


    search_fields = 'name', 'state__name', 'telephone'
    ordering = ['name']

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'export_url': '/jurisdictions/emails',
            'export_caption': 'Download Jurisdiction Emails',
            'show_export_button': True
        }

        return super(JurisdictionAdmin, self).changelist_view(
            request, extra_context)


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
        tot_reqs += 1
        # Only send e-mail once
        if email_req.send_email == False:
            obj_list = email_req.jurisdiction.all()
            jurisdiction_list = []
            for jurisdiction in obj_list:
                jurisdiction_list.append([jurisdiction.name, jurisdiction.pk])
            jurisdiction_list.sort(key=lambda x: x[0])

            if ',' in email_req.recipients:
                recipient_list = email_req.recipients.split(',')
            elif '\r\n' in email_req.recipients:
                recipient_list = email_req.recipients.split('\r\n')
            elif '\n' in email_req.recipients:
                recipient_list = email_req.recipients.split('\n')
            elif ';' in email_req.recipients:
                recipient_list = email_req.recipients.split(';')
            else: #assume only one e-mail
                recipient_list = [email_req.recipients]
            
            recipient_list = [item.strip(' ') for item in recipient_list]
            
            # send email
            mail = MailSurvey(
                jurisdiction_list, recipient_list, email_req.email_text,
                subject=email_req.name)
            status = mail.send()
            if status == 'OK':
                queryset.update(send_email=True)
                count_success += 1
        else:
            count_resend += 1
        
    message = ''
    if count_success > 0:
        message += '{} out of {} e-mails were successfully sent.'.format(
            count_success, tot_reqs)
    if count_resend > 0:
        message += '{} out of {} e-mails have already been sent to their recipient. No action has been taken. To force a re-send, set "Sent E-mail?" to False'.format(count_resend, tot_reqs)
    modeladmin.message_user(request,  message)


def mark_unsent(modeladmin, request, queryset):
    queryset.update(send_email=False)


class SurveyEmailAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'send_email', 'recipients'
    )
    actions = [send_email, mark_unsent]

    def get_readonly_fields(self, request, obj=None):
        return ['send_email']


send_email.short_description = 'Send e-mail'
mark_unsent.short_description = 'Mark e-mail as not sent'
admin.site.register(State, StateAdmin)
admin.site.register(SurveyEmail, SurveyEmailAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
