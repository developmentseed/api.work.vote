from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from survey.views import ContactViewSet
from .views import JurisdictionViewSet, StateViewSet, SearchViewSet, PageViewSet
from .SurveyResponses.survey_responses import GetSurveyResponse


router = DefaultRouter()
router.register(r'contacts', ContactViewSet.as_view(), 'contacts')
router.register(r'states', StateViewSet.as_view(), 'states')
router.register(r'search', SearchViewSet.as_view(), 'search')
router.register(r'pages', PageViewSet.as_view(), 'pages')
router.register(r'jurisdictions', JurisdictionViewSet.as_view(), 'jurisdictions')

# Redirect root to ReadMe.io
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^response/$', GetSurveyResponse, name='response'),
    url(r'^', include(router.urls))
]
