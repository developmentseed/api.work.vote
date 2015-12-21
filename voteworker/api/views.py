from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.gis.geos import Point

from .serializer import StateSerializer, JurisdictionSerializer
from jurisdiction.models import State, Jurisdiction


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = State.objects.all()
    serializer_class = StateSerializer


class JurisdictionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Jurisdiction.objects.all()
    serializer_class = JurisdictionSerializer

    # Build the queryset based on params
    def get_queryset(self):
        request = self.request

        # Return latest processed images first
        queryset = self.queryset.extra(order_by=['name'])

        if 'contains' in request.GET:
            coords = request.GET.get('contains').split(',')
            coords = map(float, coords)
            pnt = Point(coords[1], coords[0])
            queryset = queryset.filter(geometry__contains=pnt)

        if 'name' in request.GET:
            name = request.GET.get('name')
            queryset = queryset.filter(name=name)

        if 'state' in request.GET:
            state = request.GET.get('state')
            queryset = queryset.filter(state__name=state)

        return queryset
