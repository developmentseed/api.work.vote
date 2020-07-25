# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from apps.api import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
admin.site.site_url = settings.SITE_URL

urlpatterns = [
                  path('', include('apps.api.urls')),

                  # Uncomment the next line to enable the admin:
                  path('jet/', include('jet.urls', 'jet')),
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  # Django JET dashboard URLS
                  path('admin/', admin.site.urls),
                  path('tinymce/', include('tinymce.urls')),
                  path('chaining/', include('smart_selects.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
