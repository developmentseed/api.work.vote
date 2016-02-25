import re
from rest_framework import serializers

from jurisdiction.models import Jurisdiction, State


def add_city_string(obj):

    match = re.search('(city|county|City|County)', obj.name)

    if not match:
        if obj.city:
            name = '%s (city)' % obj.name
        else:
            name = '%s County' % obj.name
    else:
        name = obj.name

    return name


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

        context['name'] = add_city_string(instance)

        return context

    class Meta:
        model = Jurisdiction
        exclude = ['geometry', 'notes', 'created_at', 'updated_at']
