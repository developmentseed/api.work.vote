from django.urls import include, path
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
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('response/', GetSurveyResponse, name='response'),
]
