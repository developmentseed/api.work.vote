from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.gis.geos import Point
import geocoder

from .serializer import StateSerializer, JurisdictionSerializer
from jurisdiction.models import State, Jurisdiction


def geocode(address, required_precision_km=1.):
    """ Identifies the coordinates of an address
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
    geocoded = geocoder.google(address)
    (lat, lon) = geocoded.geometry['coordinates']
    return [lat, lon]


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = State.objects.filter(is_active=True).order_by('name')
    serializer_class = StateSerializer


class JurisdictionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Jurisdiction.objects.filter(state__is_active=True)
    serializer_class = JurisdictionSerializer

    # Build the queryset based on params
    def get_queryset(self):
        request = self.request

        # Return latest processed images first
        queryset = self.queryset.extra(order_by=['name'])

        if 'search' in request.GET:
            search = request.GET.get('search')
            county = queryset.filter(name__istartswith=search)

            print county

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
            queryset = queryset.filter(state__name=state)

        return queryset
