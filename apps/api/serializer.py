import re
from rest_framework import serializers

from jurisdiction.models import Jurisdiction, State


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ['created_at', 'updated_at']


class StateSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ['alpha']


class JurisdictionSerializer(serializers.ModelSerializer):

    state = StateSummarySerializer()

    def to_representation(self, instance):
        context = super(JurisdictionSerializer, self).to_representation(instance)
        match = re.search('(city|county|City|County)', instance.name)

        if not match:
            if instance.city:
                context['name'] = '%s (city)' % instance.name
            else:
                context['name'] = '%s County' % instance.name

        return context

    class Meta:
        model = Jurisdiction
        exclude = ['geometry', 'notes', 'created_at', 'updated_at']
