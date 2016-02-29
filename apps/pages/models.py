from tinymce.models import HTMLField
from django.contrib.gis.db import models


class Page(models.Model):

    title = models.CharField('Post Title', max_length=250)
    content = HTMLField('Post content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Page is published?', default=True)

    def __unicode__(self):
        return self.title