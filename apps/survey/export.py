import csv
from django.http import HttpResponse
# from django.utils.encoding import smart_str

from survey.models import Application, Survey

def smart_str(x):
    if isinstance(x, unicode):
        return unicode(x).encode("utf-8")
    elif isinstance(x, int) or isinstance(x, float):
        return str(x)
    return x


def base_export(model):

    jurisdictions = model.objects.all()

    r = HttpResponse(content_type='text/csv')
    r['Content-Disposition'] = 'attachment; filename=%s.csv' % model._meta.model_name
    writer = csv.writer(r, csv.excel)
    r.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    fields = [f for f in model._meta.get_all_field_names()]
    headings = [smart_str(f) for f in fields]

    writer.writerow(headings)

    for j in jurisdictions:
        row = []
        for f in fields:
            row.append(getattr(j, f))
        writer.writerow(row)

    return r


def export_applications():
    return base_export(Application)


def export_surveys():
    return base_export(Survey)
