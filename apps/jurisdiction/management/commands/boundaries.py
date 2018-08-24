import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry

from state_dict import state_name_crosswalk

from jurisdiction.models import Jurisdiction, State


def prepare(path):
    """ Receives a GeoJson and returns a python object """

    f = open(path, 'U')
    obj = json.loads(f.read())

    return obj


def save_geometry(obj):
    """ Saves geometries of jurisdictions in each state """
    resp = {}

    for feature in obj['features']:

        state = feature['properties']['STATEFP']
        name = feature['properties']['NAME']
        geometry = feature['geometry']
        """
        if feature['properties']['FUNCSTAT'] == 'F' and state == '51':
            city = True
        else:
        """
        # Skip Virginia for now
        if state == '51':
            continue
        city = False

        try:
            try:
                j = Jurisdiction.objects.get(state_id=int(state), name=name, city=city)
            except Jurisdiction.DoesNotExist:
                try:
                    s = State.objects.get(id=int(state))
                except State.DoesNotExist:
                    try:
                        s = State(id=int(state), name=state_name_crosswalk[int(state)]['name'],alpha=state_name_crosswalk[int(state)]['abbr'], is_active = True)
                        s.save()
                    except KeyError: # territories
                        continue
                # Set display option to "No" since we don't have any real data yet
                j = Jurisdiction(state_id=int(state), name=name, city=city, display = 'N')

            mpolygons = GEOSGeometry(json.dumps(geometry))
            j.geometry = mpolygons
            j.save()

            if j.state.name in resp:
                resp[j.state.name].append(name)
            else:
                resp[j.state.name] = [name]

        except Jurisdiction.DoesNotExist:
            s = State.objects.get(id=int(state))
            print '%s was not found in %s' % (name, s)

    return resp


class Command(BaseCommand):
    help = 'Import jurisdiction boundaries'

    def handle(self, *args, **options):
        p = prepare(str(settings.BASE_DIR.path('apps/jurisdiction/voteworker2017.geojson')))
        s = save_geometry(p)

        for k, v in s.iteritems():
            self.stdout.write('%s: %s jurisdictions' % (k, len(v)))
