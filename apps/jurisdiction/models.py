from django.contrib.gis.db import models
from smart_selects.db_fields import ChainedManyToManyField
from tinymce.models import HTMLField


class State(models.Model):
    name = models.CharField('State', max_length=250)
    alpha = models.CharField('Alpha-2 Code', max_length=2)
    pollworker_website = models.CharField('State Poll worker website', max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Whether state is active', default=True)
    notes = models.TextField('Notes', null=True, blank=True)

    def __str__(self):
        return self.name


class Zipcode(models.Model):
    code = models.CharField('Zip Code', max_length=5, primary_key=True)
    state = models.ForeignKey(State)
    geometry = models.MultiPolygonField('zipcode Geometry', null=True, blank=True)

    def __str__(self):
        return self.code


DISPLAY_OPTIONS = (
    ('Y', 'Display Information'),
    ('N', 'No information displayed')
)


class Jurisdiction(models.Model):
    name = models.CharField('Jurisdiction Name', max_length=250)
    state = models.ForeignKey(State)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    obtained_at = models.DateField('Date obtained', null=True, blank=True)
    website = models.CharField('info website', max_length=400, null=True, blank=True)
    application = models.CharField('online application', max_length=400, null=True, blank=True)
    telephone = models.CharField('telephone', max_length=250, null=True, blank=True)
    email = models.CharField('email', max_length=250, null=True, blank=True)
    office_address = models.TextField('office address', null=True, blank=True)
    mailing_address = models.TextField('mailing address (if different)', null=True, blank=True)
    how_obtained = models.TextField('how data obtained', null=True, blank=True)
    registration_status = models.TextField(
        'Registered in the state OR registered in the jurisdiction?'
        ' - Input: S or J', null=True, blank=True)
    pre_registration = models.TextField(
        'If pre-registration is available, is it required for 16/17 yo\'s?'
        ' - Input: Y or N', null=True, blank=True)
    voter_registration_url = models.CharField(
        'Website for online voter regisration', max_length=300,
        blank=True, null=True)
    minimum_age = models.CharField('Minimum age - Input: ##', max_length=250, null=True, blank=True)
    high_school_student = models.TextField('Can high school students work? - Input: Y or N', null=True, blank=True)
    hours_start = models.CharField('Hours start', max_length=250, null=True, blank=True)
    hours_end = models.CharField('Hours end', max_length=250, null=True, blank=True)
    full_day_req = models.TextField('Full Day required - Input: Y or N', null=True, blank=True)
    split_days_allowed = models.TextField(
        'If split days are allowed, must one find a buddy? Input: Y or N',
        null=True, blank=True)
    compensation = models.TextField(
        'Pay/compensation for the day - Input: Total amount OR hourly rate OR'
        ' a range from min to max if the pay varies based on position.',
        null=True, blank=True)
    interview = models.TextField('Interview requirement - Input: Y or N', null=True, blank=True)
    training = models.TextField('Training - Input: Y or N', null=True, blank=True)
    complete_training = models.TextField('Complete training for each election? - Input: Y or N',
                                         null=True, blank=True)
    post_training_exam = models.TextField('Pass a post-training exam or assessment - Input: Y or N',
                                          null=True, blank=True)
    must_have_email = models.TextField(
        'Must have an email address and access to a computer and internet - Input:'
        ' Y or N', null=True, blank=True)
    candidate_prohibition = models.TextField(
        'Prohibition on being a candidate or related to a candidate - Y or N',
        null=True, blank=True)
    notes = models.TextField('Notes', null=True, blank=True)
    geometry = models.MultiPolygonField('Jurisdiction Geometry', null=True, blank=True)
    city = models.BooleanField('Whether the jurisdiction is a city', default=False)
    further_notes = models.TextField('Further Notes', null=True, blank=True)
    display = models.CharField(max_length = 1, choices = DISPLAY_OPTIONS, default='Y')
    student_website = models.CharField('Website for Student Pollworker Program', max_length=400, null=True, blank=True)
    city_model = models.ForeignKey('self', blank=True, null=True)
    city_sub = models.CharField('text for the message in the sub',  max_length=250,  null=True, blank=True)

    def __str__(self):
        return self.name + ', ' + self.state.name


class SurveyEmail(models.Model):
    """ Model for tracking and sending emails to election officials """
    name = models.CharField(
        'Email label',
        help_text='Used as display name and as email subject line.',
        max_length=250)
    recipients = models.TextField('List of emails', help_text='Use commas, semicolons or line breaks to separate emails. Do not enter e-mail addresses containing those special characters.')
    email_text = HTMLField('E-mail text', help_text='This text will be displayed above the survey links.', default = 'Thank you for your participation in our survey for WorkElections.com. Please click on the link corresponding with the jurisdiction for which you would like to update information.')
    state = models.ForeignKey(State, default=1)
    jurisdiction = ChainedManyToManyField(Jurisdiction, chained_field='state',
                                          chained_model_field='state')
    send_email = models.BooleanField(
        'Sent email?',
        help_text = 'To edit this field, use the dropdown on the summary view.',
        default = False)

    def __unicode__(self):
        return self.name
