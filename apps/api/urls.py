from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from survey.views import ContactViewSet
from .views import JurisdictionViewSet, StateViewSet, SearchViewSet, PageViewSet
from .SurveyResponses.survey_responses import GetSurveyResponse


router = DefaultRouter()
router.register(r'contacts', ContactViewSet, 'contacts')
router.register(r'states', StateViewSet, 'states')
router.register(r'search', SearchViewSet, 'search')
router.register(r'pages', PageViewSet, 'pages')
router.register(r'jurisdictions', JurisdictionViewSet, 'jurisdictions')

# Redirect root to ReadMe.io
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^response/$', GetSurveyResponse, name='response'),
    url(r'^', include(router.urls))
]
