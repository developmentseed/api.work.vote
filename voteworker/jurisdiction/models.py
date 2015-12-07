from django.db import models


class State(models.Model):

    name = models.CharField('State', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


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
    office_address = models.CharField('office address', max_length=250, null=True, blank=True)
    mailing_address = models.CharField('mailing address (if different)', max_length=250, null=True, blank=True)
    how_obtained = models.CharField('how data obtained', max_length=250, null=True, blank=True)
    registration_status = models.CharField('Registered in the state OR registered in the jurisdiction? - Input: S or J', max_length=250, null=True, blank=True)
    pre_registration = models.CharField('If pre-registration is available, is it required for 16/17 yo\'s? - Input: Y or N', max_length=250, null=True, blank=True)
    minimum_age = models.CharField('Minimum age - Input: ##', max_length=250, null=True, blank=True)
    high_school_student = models.CharField('Can high school students work? - Input: Y or N', max_length=250, null=True, blank=True)
    hours_start = models.CharField('Hours start', max_length=250, null=True, blank=True)
    hours_end = models.CharField('Hours end', max_length=250, null=True, blank=True)
    full_day_req = models.CharField('Full Day required - Input: Y or N', max_length=250, null=True, blank=True)
    split_days_allowed = models.CharField('If split days are allowed, must one find a buddy? Input: Y or N', max_length=250, null=True, blank=True)
    compensation = models.CharField('Pay/compensation for the day - Input: Total amount OR hourly rate OR a range from min to max if the pay varies based on position.', max_length=250, null=True, blank=True)
    interview = models.CharField('Interview requirement - Input: Y or N', max_length=250, null=True, blank=True)
    training = models.CharField('Training - Input: Y or N', max_length=250, null=True, blank=True)
    complete_training = models.CharField('Complete training for each election? - Input: Y or N', max_length=250, null=True, blank=True)
    post_training_exam = models.CharField('Pass a post-training exam or assessment - Input: Y or N', max_length=250, null=True, blank=True)
    must_have_email = models.CharField('Must have an email address and access to a computer and internet - Input: Y or N', max_length=250, null=True, blank=True)
    candidate_prohibition = models.CharField('Prohibition on being a candidate or related to a candidate - Y or N', max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.name
