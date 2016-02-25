from jsonfield import JSONField
from django_enumfield import enum
from django.contrib.gis.db import models


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
