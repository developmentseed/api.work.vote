from rest_framework import serializers

from jurisdiction.models import Jurisdiction, State


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State


class JurisdictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jurisdiction
