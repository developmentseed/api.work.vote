import json
import os
import spatialite 

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from jurisdiction.models import Jurisdiction, State, Zipcode

directory = 'exports'

def saveZipcodes(records):
    print('Saving via bulk update') 
    try:
        zipcodes = [Zipcode(**obj) for obj in records]
        Zipcode.objects.bulk_create(zipcodes)
        objs = []
    except:
        for obj in records:
            try:
                Zipcode.objects.get(code=obj['code'])
            except Zipcode.DoesNotExist:
                obj = Zipcode(**obj)
                obj.save()

class Command(BaseCommand):
    help = 'Export data'

    def handle(self, *args, **options):
        print('Import data')

        conn = spatialite.connect('zipcodes.db')
        cursor = conn.cursor()

        cursor.execute('SELECT code, meta, ST_AsText(geometry) as geom FROM zipcodes')
        # results = cursor.fetchall()

        objs = []
        while (True):
            r = cursor.fetchone()
            if not r:
                break
            meta = json.loads(r[1])
            state_id = int(meta['STATEFP10'])
            obj = {
                'code': r[0],
                'state_id': state_id,
                'geometry': GEOSGeometry(r[2])
            }
            objs.append(obj)
            print('Preparing zipcode %s' % r[0])

            if len(objs) > 1000:
                saveZipcodes(objs)
                objs = []

        saveZipcodes(objs)


       
        
        # make sure export folder exists
        # if not os.path.exists(directory):
        #     raise Exception('exports folder is not there')
        
        # # load states first
        # ## make sure states folder exists
        # state_path = os.path.join(directory, 'states')
        # if not os.path.exists(state_path):
        #     raise Exception('%s folder is missing' % state_path)
        
        # ## read all the state json files
        # state_files = os.listdir(state_path)

        # for file in state_files:
        #     with open(os.path.join(state_path, file)) as f:
        #         state = json.load(f)
        #         State.objects.update_or_create(**state)
        #         print('record for %s saved' % state['name'])


        # # load jurisdictions
        # ## make sure jurisdiction folder exists
        # jr_path = os.path.join(directory, 'jurisdictions')
        # if not os.path.exists(jr_path):
        #     raise Exception('%s folder is missing' % jr_path)
        
        # ## read all the state json files
        # state_folders = os.listdir(jr_path)

        # for state in state_folders:
        #     jr_folder = os.path.join(jr_path, state)
        #     jr_files = os.listdir(jr_folder)
        #     for jr in jr_files:
        #         jr_file = os.path.join(jr_folder, jr)
        #         with open(jr_file) as f:
        #             geojson = json.load(f)
        #             record = geojson['properties']

        #             # get state
        #             record['state'] = State.objects.get(pk=record['state'])

        #             record['geometry'] = GEOSGeometry(json.dumps(geojson['geometry']))
        #             Jurisdiction.objects.update_or_create(**record)
        #             print('record for %s saved' % record['name'])



