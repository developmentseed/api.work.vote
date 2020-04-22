from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from .models import Jurisdiction, State, SurveyEmail
from mailman import mailer
from django import forms


class JurisdictionAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JurisdictionAdminForm, self).__init__(*args, **kwargs)
        self.fields['city_model'].queryset = Jurisdiction.objects.filter(
            city=True).order_by('name')


class JurisdictionAdmin(admin.ModelAdmin):
    list_display = 'name', 'state', 'website', 'telephone', 'email', 'city'
    list_filter = 'state', 'city'
    fields = (
        'name', 'state',
        'display', 'city','city_model', 'city_sub',
        'obtained_at',
        'website', 'application', 'student_website',
        'telephone', 'email',
        'office_address', 'mailing_address',
        'hours_start', 'hours_end',
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
    form = JurisdictionAdminForm

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
            recipient_list = mailer.clean_emails(email_req.recipients)
            # send email
            mail = mailer.MailSurvey(
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


def get_csv_survey_links(modeladmin, request, queryset):
    del modeladmin, request
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="survey_email_links.csv"'
    for email_req in queryset:
        juris = sorted((j.name, j.pk) for j in email_req.jurisdiction.all())
        for name, pk in juris:
            survey_link = settings.SURVEY_MONKEY_URL.format(pk)
            response.write('%s,%s\n' % (name, survey_link))
        response.write('\n')
    return response


class SurveyEmailAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'send_email', 'recipients'
    )
    actions = [send_email, mark_unsent, get_csv_survey_links]

    def get_readonly_fields(self, request, obj=None):
        return ['send_email']


send_email.short_description = 'Send e-mail'
mark_unsent.short_description = 'Mark e-mail as not sent'
admin.site.register(State, StateAdmin)
admin.site.register(SurveyEmail, SurveyEmailAdmin)
admin.site.register(Jurisdiction, JurisdictionAdmin)
