import re
from rest_framework import serializers

from pages.models import Page
from jurisdiction.models import Jurisdiction, State


def add_city_string(obj):
    match = re.search(
            '(city|county|region|City|County|Region)',
            obj.name)
    if match:
        return obj.name
    if obj.city:
        return '%s (City)' % obj.name
    else:
        return '%s County' % obj.name


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page


class StateSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        topojson_ids = {"AL":{"id":"1","code":"AL","name":"Alabama"},"AK":{"id":"2","code":"AK","name":"Alaska"},"AZ":{"id":"4","code":"AZ","name":"Arizona"},"AR":{"id":"5","code":"AR","name":"Arkansas"},"CA":{"id":"6","code":"CA","name":"California"},"CO":{"id":"8","code":"CO","name":"Colorado"},"CT":{"id":"9","code":"CT","name":"Connecticut"},"DE":{"id":"10","code":"DE","name":"Delaware"},"DC":{"id":"11","code":"DC","name":"District of Columbia"},"FL":{"id":"12","code":"FL","name":"Florida"},"GA":{"id":"13","code":"GA","name":"Georgia"},"HI":{"id":"15","code":"HI","name":"Hawaii"},"ID":{"id":"16","code":"ID","name":"Idaho"},"IL":{"id":"17","code":"IL","name":"Illinois"},"IN":{"id":"18","code":"IN","name":"Indiana"},"IA":{"id":"19","code":"IA","name":"Iowa"},"KS":{"id":"20","code":"KS","name":"Kansas"},"KY":{"id":"21","code":"KY","name":"Kentucky"},"LA":{"id":"22","code":"LA","name":"Louisiana"},"ME":{"id":"23","code":"ME","name":"Maine"},"MD":{"id":"24","code":"MD","name":"Maryland"},"MA":{"id":"25","code":"MA","name":"Massachusetts"},"MI":{"id":"26","code":"MI","name":"Michigan"},"MN":{"id":"27","code":"MN","name":"Minnesota"},"MS":{"id":"28","code":"MS","name":"Mississippi"},"MO":{"id":"29","code":"MO","name":"Missouri"},"MT":{"id":"30","code":"MT","name":"Montana"},"NE":{"id":"31","code":"NE","name":"Nebraska"},"NV":{"id":"32","code":"NV","name":"Nevada"},"NH":{"id":"33","code":"NH","name":"New Hampshire"},"NJ":{"id":"34","code":"NJ","name":"New Jersey"},"NM":{"id":"35","code":"NM","name":"New Mexico"},"NY":{"id":"36","code":"NY","name":"New York"},"NC":{"id":"37","code":"NC","name":"North Carolina"},"ND":{"id":"38","code":"ND","name":"North Dakota"},"OH":{"id":"39","code":"OH","name":"Ohio"},"OK":{"id":"40","code":"OK","name":"Oklahoma"},"OR":{"id":"41","code":"OR","name":"Oregon"},"PA":{"id":"42","code":"PA","name":"Pennsylvania"},"RI":{"id":"44","code":"RI","name":"Rhode Island"},"SC":{"id":"45","code":"SC","name":"South Carolina"},"SD":{"id":"46","code":"SD","name":"South Dakota"},"TN":{"id":"47","code":"TN","name":"Tennessee"},"TX":{"id":"48","code":"TX","name":"Texas"},"UT":{"id":"49","code":"UT","name":"Utah"},"VT":{"id":"50","code":"VT","name":"Vermont"},"VA":{"id":"51","code":"VA","name":"Virginia"},"WA":{"id":"53","code":"WA","name":"Washington"},"WV":{"id":"54","code":"WV","name":"West Virginia"},"WI":{"id":"55","code":"WI","name":"Wisconsin"},"WY":{"id":"56","code":"WY","name":"Wyoming"},"AS":{"id":"60","code":"AS","name":"America Samoa"},"FM":{"id":"64","code":"FM","name":"Federated States of Micronesia"},"GU":{"id":"66","code":"GU","name":"Guam"},"MH":{"id":"68","code":"MH","name":"Marshall Islands"},"MP":{"id":"69","code":"MP","name":"Northern Mariana Islands"},"PW":{"id":"70","code":"PW","name":"Palau"},"PR":{"id":"72","code":"PR","name":"Puerto Rico"},"UM":{"id":"74","code":"UM","name":"U.S. Minor Outlying Islands"},"VI":{"id":"78","code":"VI","name":"Virgin Islands of the United States"}}

        context = super(StateSerializer, self).to_representation(instance)
        try:
            context['topojson_id'] = int(topojson_ids[instance.alpha]['id'])
        except KeyError:
            context['topojson_id'] = None

        return context

    class Meta:
        model = State
        exclude = ['created_at', 'updated_at']


class StateSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ['alpha']

class CityModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jurisdiction
        fields = ['id','name']

class JurisdictionSummarySerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        context = super(JurisdictionSummarySerializer, self).to_representation(instance)
        context['name'] = add_city_string(instance)

        return context

    class Meta:
        model = Jurisdiction
        fields = ['id', 'name']


class JurisdictionSerializer(JurisdictionSummarySerializer):

    state = StateSummarySerializer()
    city_model = CityModelSerializer(read_only=True)

    class Meta:
        model = Jurisdiction
        exclude = ['geometry', 'notes', 'created_at', 'updated_at']
