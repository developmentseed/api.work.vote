import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry

from .state_func import state_name_crosswalk

from jurisdiction.models import Jurisdiction, State
import os
import datetime

def prepare(path):
    """ Receives a GeoJson and returns a python object """

    f = open(path, 'U')
    obj = json.loads(f.read())

    return obj


def save_geometry(obj, state_name, name_var):
    """ Saves geometries of jurisdictions in each state """
    resp = {}
    # this will return only one item
    state = [k for k,v in state_name_crosswalk.items() if v['name'] ==state_name][0]
    old_data = Jurisdiction.objects.filter(state_id=state).filter(created_at__lte=datetime.date(2018, 8, 1))

    if old_data: # If there's old data in the database, be careful when deleting
        print("Old data here: {}".format(old_data))
        return resp
    else:
        print("All new data; continuing")

    # Delete counties from this state (as long as the data is old; if it's new, be sure before continuing)
    Jurisdiction.objects.filter(state_id=state).delete()

    # Add jurisdictions
    for feature in obj['features']:
        name = feature['properties'][name_var].title()
        geometry = feature['geometry']
        city = True

        try:
            j = Jurisdiction.objects.get(state_id=int(state), name=name, city=city)
        except Jurisdiction.DoesNotExist:
            j = Jurisdiction(state_id=int(state), name=name, city=city, display = 'N')
        
        mpolygons = GEOSGeometry(json.dumps(geometry))
        j.geometry = mpolygons
        j.save()

        if j.state.name in resp:
            resp[j.state.name].append(name)
        else:
            resp[j.state.name] = [name]
    return resp

class Command(BaseCommand):
    help = 'Add additional states'
    
    def handle(self, *args, **options):
        # Keep Going allows addition of multiple states at once
        keepGoing = "TRUE"
        with open('args.txt', 'r') as f:
            while keepGoing == "TRUE":
                path = next(f).strip()
                state = next(f).strip()
                name_var = next(f).strip()
                p = prepare(str(settings.BASE_DIR.path(path)))
                s = save_geometry(p, state, name_var)
                keepGoing = next(f).strip()
                for k, v in s.items():
                    self.stdout.write('%s: %s jurisdictions' % (k, len(v)))