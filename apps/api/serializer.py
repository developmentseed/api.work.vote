from rest_framework import serializers

from jurisdiction.models import Jurisdiction, State


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ['created_at', 'updated_at']


class JurisdictionSerializer(serializers.ModelSerializer):

    state = StateSerializer()

    class Meta:
        model = Jurisdiction
        exclude = ['geometry', 'notes', 'created_at', 'updated_at']
