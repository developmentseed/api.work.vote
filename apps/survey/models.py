from jsonfield import JSONField
from django_enumfield import enum
from django.contrib.gis.db import models
import csv, io

from api.SurveyResponses.survey_responses import update_db_responses

from jurisdiction.models import Jurisdiction

class AgeRange(enum.Enum):

    A16_18 = 0
    A19_25 = 1
    A26_35 = 2
    A36_50 = 3
    A51_64 = 4
    A65_older = 5


class Survey(models.Model):
    """ Model for handling survey questions """

    created_at = models.DateTimeField(auto_now_add=True)
    age_range = enum.EnumField(AgeRange, null=True, blank=True)
    languages = JSONField('What languages do you speak other than English?', null=True, blank=True)
    familiarity_w_technology = models.IntegerField(
        'How familiar are you with working with computer technology on a scale of 1 to 10?'
        ' 1 being "not familiar at all" and 10 being "extremely familiar."',
        default=0)


class Application(models.Model):
    """ Model for handling application questions """

    created_at = models.DateTimeField(auto_now_add=True)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='app_jurisdiction')
    city = models.TextField('city', null=True, blank=True)
    county = models.TextField('county', null=True, blank=True)
    age_range = enum.EnumField(AgeRange, null=True, blank=True)
    languages = JSONField('What languages do you speak other than English?', null=True, blank=True)
    familiarity_w_technology = models.IntegerField(
        'How familiar are you with working with computer technology on a scale of 1 to 5?'
        ' 1 being "not familiar at all" and 5 being "extremely familiar."',
        default=0)

class UploadFile(models.Model):

    description = models.CharField('Response Set Description', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='uploads/')

    def __unicode__(self):
        return self.description
    
    def save(self, *args, **kwargs):
        csv_file = self.document.read().decode('utf-8')
        io_string = io.StringIO(csv_file)
        to_read = csv.reader(io_string)
        questions = next(to_read)

        # Correct for Compensation formatting
        questions[13] = questions[12] + " | Upper Bound:"
        questions[12] += " | Low Bound:"

        answer_types = next(to_read)
        
        for answer_row in to_read:
            row_dict = {questions[i]: answer_row[i] for i in range(9, len(questions) -1)}
            jurisdiction_id = answer_row[len(questions) -1]
            updated, juris_info = update_db_responses(row_dict, jurisdiction_id)

        super(UploadFile, self).save(*args, **kwargs)