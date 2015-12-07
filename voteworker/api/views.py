from rest_framework import viewsets
from rest_framework import permissions


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
