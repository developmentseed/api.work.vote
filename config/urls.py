# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from api import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include(urls)),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
