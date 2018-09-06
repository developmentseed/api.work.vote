import sys
import spatialite 
import geocoder
from geocoder.mapbox import MapboxQuery

from django.db.models import Q
from jurisdiction.models import Jurisdiction
from django.contrib.gis.geos import Point, GEOSGeometry, MultiPoint
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import viewsets, permissions, status

from pages.models import Page
from jurisdiction.models import State, Jurisdiction
from jurisdiction.export import export_jurisdiction_emails
from .serializer import (StateSerializer, JurisdictionSerializer, add_city_string, JurisdictionSummarySerializer,
                         PageSerializer)


class NewMapboxQuery(MapboxQuery):
    """ Adds limit support to the mapbox geocoder """

    def _build_params(self, location, provider_key, **kwargs):
        params = super(NewMapboxQuery, self)._build_params(location, provider_key, **kwargs)
        params['limit'] = kwargs.get('limit', 5)
        return params

def searchZipcode(zipcode, jurisdictions):
    """ Finds matching jurisdictions for a given zipcode """
    conn = spatialite.connect('zipcodes.db')
    cursor = conn.cursor()
    try:
        if len(str(zipcode)) != 5:
            return jurisdictions.none()

        cursor.execute('SELECT ST_AsText(geometry) as geom FROM zipcodes WHERE code=?', (int(zipcode), ))
        results = cursor.fetchone()
        if type(results) is tuple:
            geometry = GEOSGeometry(results[0])
            return jurisdictions.filter(geometry__intersects=geometry)
        else:
            return jurisdictions.none()
    except:
        return jurisdictions.none()


def geocode(address, jurisdictions, required_precision_km=1., limit=20):
    """ Find jurisdictions that match a given address Identifies the coordinates of an address. It will ignore the input
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
        if len(geocoded) > 0:
            multipoints = MultiPoint([GEOSGeometry(item.wkt) for item in geocoded])
            return jurisdictions.filter(geometry__intersects=multipoints)
        return jurisdictions.none()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return jurisdictions.none()


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
    queryset = Jurisdiction.objects.filter(state__is_active=True)
    serializer_class = JurisdictionSerializer

    @list_route()
    def emails(self, request):
        if request.user.is_authenticated():
            return export_jurisdiction_emails()
        else:
            return Response({'detail': 'Not allowed'},
                            status=status.HTTP_401_UNAUTHORIZED)

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

    def list(self, request):

        response = []
        if 'q' in request.GET:
                    # statees
            states = State.objects.order_by('name')

            # jurisdictions
            jurisdictions = Jurisdiction.objects.filter(state__is_active=True).extra(order_by=['name'])

            query = request.GET.get('q')

            # look for zipcodes
            zipcodes = searchZipcode(query, jurisdictions)

            # look for geocodes
            if not zipcodes:
                geocodes = geocode(query, jurisdictions)
                names = jurisdictions.filter(name__istartswith=query)

                jurisdictions = zipcodes | geocodes | names
            else:
                jurisdictions = zipcodes

            if jurisdictions:
                for jur in jurisdictions:

                    response.append({
                        'type': 'jurisdiction',
                        'id': jur.id,
                        'name': add_city_string(jur),
                        'state_id': jur.state.id,
                        'state_alpha': jur.state.alpha
                    })

            # look for states
            filtered_states = states.filter(name__istartswith=query)
            if filtered_states:
                for state in filtered_states:
                    response.append({
                        'type': 'state',
                        'id': state.id,
                        'name': state.name
                    })

        return Response(response, status=status.HTTP_200_OK)
