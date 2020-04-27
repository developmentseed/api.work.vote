import json
import os

from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.core.management.base import BaseCommand
from jurisdiction.models import Jurisdiction, State

directory = 'exports'

def mkdirp(path):
    if not os.path.exists(path):
        os.makedirs(path)

def record2geojson(record, fields, folder='jurisdiction'):
    state = record.state.name.lower() 
    path = os.path.join(directory, folder, state)
    mkdirp(path)
    if record.geometry:
        geometry = record.geometry.geojson
        obj = model_to_dict(record, fields=fields)

        geojson ={
            "type": "Feature",
            "properties": obj,
            "geometry": json.loads(geometry)
        }

        filename = '%s.geojson' % record.name.lower().replace(' ', '_')
        with open(os.path.join(path, filename), 'w') as outfile:
            outfile.write(json.dumps(geojson, cls=DjangoJSONEncoder))
        print('stored %s: %s' % (state, record.name))

def state2json(record):
    path = os.path.join(directory, 'states')
    mkdirp(path)

    filename = '%s.json' % record.name.lower()
    with open(os.path.join(path, filename), 'w') as outfile:
        outfile.write(json.dumps(model_to_dict(record), cls=DjangoJSONEncoder))
    print('stored %s' % record.name)


class Command(BaseCommand):
    help = 'Export jurisdiction boundaries'

    def handle(self, *args, **options):
        print('Exporting Jurisdictions')
        fields = [f.name for f in Jurisdiction._meta.get_fields() if f.name != 'geometry']
        js = Jurisdiction.objects.all()
        [record2geojson(j, fields) for j in js]

        print('Exporting states')
        states = State.objects.all()
        [state2json(s) for s in states]
