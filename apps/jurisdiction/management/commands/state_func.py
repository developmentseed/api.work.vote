from django.conf import settings
from django.core.management.base import BaseCommand

from jurisdiction.models import Jurisdiction, State

state_name_crosswalk = {1: {'name': 'Alabama', 'abbr': 'AL'}, 2: {'name': 'Alaska', 'abbr': 'AK'}, 4: {'name': 'Arizona', 'abbr': 'AZ'}, 
                        5: {'name': 'Arkansas', 'abbr': 'AR'}, 6: {'name': 'California', 'abbr': 'CA'}, 8: {'name': 'Colorado', 'abbr': 'CO'}, 
                        9: {'name': 'Connecticut', 'abbr': 'CT'}, 10: {'name': 'Delaware', 'abbr': 'DE'}, 11: {'name': 'District of Columbia', 'abbr': 'DC'}, 
                        12: {'name': 'Florida', 'abbr': 'FL'}, 13: {'name': 'Georgia', 'abbr': 'GA'}, 15: {'name': 'Hawaii', 'abbr': 'HI'}, 
                        16: {'name': 'Idaho', 'abbr': 'ID'}, 17: {'name': 'Illinois', 'abbr': 'IL'}, 18: {'name': 'Indiana', 'abbr': 'IN'}, 
                        19: {'name': 'Iowa', 'abbr': 'IA'}, 20: {'name': 'Kansas', 'abbr': 'KS'}, 21: {'name': 'Kentucky', 'abbr': 'KY'}, 
                        22: {'name': 'Louisiana', 'abbr': 'LA'}, 23: {'name': 'Maine', 'abbr': 'ME'}, 24: {'name': 'Maryland', 'abbr': 'MD'}, 
                        25: {'name': 'Massachusetts', 'abbr': 'MA'}, 26: {'name': 'Michigan', 'abbr': 'MI'}, 27: {'name': 'Minnesota', 'abbr': 'MN'}, 
                        28: {'name': 'Mississippi', 'abbr': 'MS'}, 29: {'name': 'Missouri', 'abbr': 'MO'}, 30: {'name': 'Montana', 'abbr': 'MT'}, 
                        31: {'name': 'Nebraska', 'abbr': 'NE'}, 32: {'name': 'Nevada', 'abbr': 'NV'}, 33: {'name': 'New Hampshire', 'abbr': 'NH'}, 
                        34: {'name': 'New Jersey', 'abbr': 'NJ'}, 35: {'name': 'New Mexico', 'abbr': 'NM'}, 36: {'name': 'New York', 'abbr': 'NY'}, 
                        37: {'name': 'North Carolina', 'abbr': 'NC'}, 38: {'name': 'North Dakota', 'abbr': 'ND'}, 39: {'name': 'Ohio', 'abbr': 'OH'}, 
                        40: {'name': 'Oklahoma', 'abbr': 'OK'}, 41: {'name': 'Oregon', 'abbr': 'OR'}, 42: {'name': 'Pennsylvania', 'abbr': 'PA'}, 
                        44: {'name': 'Rhode Island', 'abbr': 'RI'}, 45: {'name': 'South Carolina', 'abbr': 'SC'}, 46: {'name': 'South Dakota', 'abbr': 'SD'}, 
                        47: {'name': 'Tennessee', 'abbr': 'TN'}, 48: {'name': 'Texas', 'abbr': 'TX'}, 49: {'name': 'Utah', 'abbr': 'UT'}, 
                        50: {'name': 'Vermont', 'abbr': 'VT'}, 51: {'name': 'Virginia', 'abbr': 'VA'}, 53: {'name': 'Washington', 'abbr': 'WA'}, 
                        54: {'name': 'West Virginia', 'abbr': 'WV'}, 55: {'name': 'Wisconsin', 'abbr': 'WI'}, 56: {'name': 'Wyoming', 'abbr': 'WY'}}

class Command(BaseCommand):
    help = 'Correct State IDs in the database'

    def handle(self, *args, **options):
        for s in State.objects.all():
            ID = s.id
            base_state = State.objects.get(id=int(ID))
            if base_state.id in state_name_crosswalk.keys() and base_state.alpha != state_name_crosswalk[base_state.id]['abbr']:
                new_state = State.objects.get(id=int(ID))
                print("Here for {}, because state.alpha is {} and abbr associated with this ID({}) is {}".format(
                    base_state.name, base_state.alpha, base_state.id, state_name_crosswalk[base_state.id]['abbr']))
                print([k for k,v in state_name_crosswalk.items() if v['abbr'] ==base_state.alpha])
                new_state.id = [k for k,v in state_name_crosswalk.items() if v['abbr'] ==base_state.alpha][0]
                base_state.delete()
                print("state.id is now {}".format(new_state.id))
                new_state.save()
            elif base_state.id == 31: # correct Nebraska spelling
                print("{} should be {}".format(base_state.name, state_name_crosswalk[base_state.id]['name']))
                base_state.name = state_name_crosswalk[base_state.id]['name']
                base_state.save()