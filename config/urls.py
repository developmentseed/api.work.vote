# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from api import urls
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
admin.site.site_url = settings.SITE_URL


urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^', include(urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
