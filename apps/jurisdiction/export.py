import csv
from django.http import HttpResponse
# from django.utils.encoding import smart_str

from jurisdiction.models import Jurisdiction

def smart_str(x):
    if isinstance(x, unicode):
        return unicode(x).encode("utf-8")
    elif isinstance(x, int) or isinstance(x, float):
        return str(x)
    return x


def export_jurisdiction_emails():

    jurisdictions = Jurisdiction.objects.filter(email__isnull=False)

    r = HttpResponse(content_type='text/csv')
    r['Content-Disposition'] = 'attachment; filename=jurisdiction_emails.csv'
    writer = csv.writer(r, csv.excel)
    r.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)

    headings = [
        smart_str(u"jurisdiction_id"),
        smart_str(u"name"),
        smart_str(u"state"),
        smart_str(u"email")
    ]

    writer.writerow(headings)

    for j in jurisdictions:
        row = [
            smart_str(j.id),
            smart_str(j.name),
            smart_str(j.state.name),
            smart_str(j.email)
        ]
        writer.writerow(row)

    return r
