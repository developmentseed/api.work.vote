from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import JurisdictionViewSet, StateViewSet


router = DefaultRouter()
router.register(r'states', StateViewSet, 'states')
router.register(r'jurisdictions', JurisdictionViewSet, 'jurisdictions')

# Redirect root to ReadMe.io
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
