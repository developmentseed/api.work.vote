import sys
import json
import spatialite 
import geocoder
from geocoder.mapbox import MapboxQuery

from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from jurisdiction.models import Jurisdiction
from django.contrib.gis.geos import Point, GEOSGeometry, MultiPoint
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status

from pages.models import Page
from jurisdiction.models import State, Jurisdiction, Zipcode
from jurisdiction.export import export_jurisdiction_emails
from .serializer import (StateSerializer, JurisdictionSerializer, format_jurisdiction_name, JurisdictionSummarySerializer,
                         PageSerializer)


class NewMapboxQuery(MapboxQuery):
    """ Adds limit support to the mapbox geocoder """

    def _build_params(self, location, provider_key, **kwargs):
        params = super(NewMapboxQuery, self)._build_params(location, provider_key, **kwargs)
        params['limit'] = kwargs.get('limit', 5)
        return params

def searchZipcode(zipcode, jurisdictions):
    """ Finds matching jurisdictions for a given zipcode """
    try:
        if len(str(zipcode)) != 5:
            return jurisdictions.none()

        zipcode = Zipcode.objects.get(code=zipcode)
        j = jurisdictions.filter(geometry__intersects=zipcode.geometry)
        return j
    except Exception as e:
        print(e)
        return jurisdictions.none()


def geocode(address, jurisdictions, required_precision_km=1., limit=5):
    """Find jurisdictions that match a given address.

    Identifies the coordinates of an address. It will ignore the input
    if it is only digits and less than 5 digits. If the input is only 5 digits
    the function assumes that is is a zipcode and search for zipcodes

    :param address:
        the address to be geocoded
    :type value:
        String
    :param required_precision_km:
        the maximum permissible geographic uncertainty for the geocoding
    :type required_precision_km:
        float
    :returns:
        dict
    :example:
        >>> geocode('1600 Pennsylvania Ave NW, Washington, DC 20500')
        {'lat': 38.89767579999999, 'lon': -77.0364827}
    """
    try:
        key = 'pk.eyJ1IjoiZGV2c2VlZCIsImEiOiJnUi1mbkVvIn0.018aLhX0Mb0tdtaT2QNe2Q'
        geocoded = NewMapboxQuery(address, key=key, country='us', limit=limit)
        results = []
        if len(geocoded) > 0:
            for item in geocoded:
                multipoints = MultiPoint([GEOSGeometry(item.wkt)])
                for jurisdiction in jurisdictions.filter(geometry__intersects=multipoints):
                    if not jurisdiction in results:
                        results.append(jurisdiction)
            return results
        return []
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return []


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = State.objects.filter(
        Q(is_active=True) | ~Q(pollworker_website='') | Q(pollworker_website__isnull=True)
    ).order_by('name')
    serializer_class = StateSerializer


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer


class JurisdictionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Jurisdiction.objects.filter()
    serializer_class = JurisdictionSerializer

    @action(detail=False)
    def emails(self, request):
        if request.user.is_authenticated():
            return export_jurisdiction_emails()
        else:
            return Response({'detail': 'Not allowed'},
                            status=status.HTTP_401_UNAUTHORIZED)
    
    # @detail_route()
    @action(detail=True)
    def geojson(self, request, pk):
        geometry = self.queryset.get(pk=pk).geometry
        if not geometry:
            return Response({})
        return Response(json.loads(geometry.geojson))

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """

        summary = self.request.GET.get('summary', False)

        if summary:
            kwargs['context'] = self.get_serializer_context()
            return JurisdictionSummarySerializer(*args, **kwargs)
        else:
            return super(JurisdictionViewSet, self).get_serializer(*args, **kwargs)

    def paginate_queryset(self, queryset):
        summary = self.request.GET.get('summary', False)

        if summary:
            return None
        else:
            return super(JurisdictionViewSet, self).paginate_queryset(queryset)

    # Build the queryset based on params
    def get_queryset(self):
        request = self.request

        # Return latest processed images first
        queryset = self.queryset.extra(order_by=['name'])

        if 'search' in request.GET:
            search = request.GET.get('search')
            county = queryset.filter(name__istartswith=search)

            if not county:
                coords = geocode(search)

                if coords:
                    pnt = Point(*coords)
                    queryset = queryset.filter(geometry__contains=pnt)
            else:
                queryset = county

        if 'contains' in request.GET:
            coords = request.GET.get('contains').split(',')
            coords = map(float, coords)
            pnt = Point(*coords)
            queryset = queryset.filter(geometry__contains=pnt)

        if 'name' in request.GET:
            name = request.GET.get('name')
            queryset = queryset.filter(name=name)

        if 'state' in request.GET:
            state = request.GET.get('state')
            queryset = queryset.filter(state__istartswith=state)

        if 'state_id' in request.GET:
            state_id = request.GET.get('state_id')
            queryset = queryset.filter(state_id=state_id)

        return queryset


class SearchViewSet(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(cache_page(60*60*60*2))
    def list(self, request):
        # jurisdictions
        jurisdictions = Jurisdiction.objects.extra(order_by=['name'])
        response = []

        if 'state' in request.GET:
            state = request.GET.get('state')
            jurisdictions = jurisdictions.filter(state__alpha=state)

        if 'q' in request.GET:
            query = request.GET.get('q')

            # look for zipcodes
            zipcodes = searchZipcode(query, jurisdictions)

            # look for geocodes
            if not zipcodes:
                geocodes = geocode(query, jurisdictions)
                names = list(jurisdictions.filter(name__istartswith=query))
                geocodes = [g for g in geocodes if g not in names]

                jurisdictions = names + geocodes
            else:
                jurisdictions = zipcodes

            if jurisdictions:
                for jur in jurisdictions:

                    response.append({
                        'type': 'jurisdiction',
                        'id': jur.id,
                        'name': format_jurisdiction_name(jur),
                        'state_id': jur.state.id,
                        'state_alpha': jur.state.alpha
                    })

        return Response(response, status=status.HTTP_200_OK)
