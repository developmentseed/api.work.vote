import csv
from django.core.management.base import BaseCommand
from django.db.models import Max
from jurisdiction.models import Jurisdiction, State

class Command(BaseCommand):
    help = 'Import from CSV.'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        parsed = []
        with open(csv_path) as f:
            reader = csv.reader(f)
            fields = next(reader)
            for row in reader:
                parsed.append(dict(zip(fields, row)))

        for record in parsed:
            record['state'] = State.objects.get(name=record['state'])
            jurisdiction = Jurisdiction.objects.create(**record)

            num_emails = len(record['email'].split(';'))
            print('record imported with %2d emails: %s' % (
                num_emails, record['name']))
