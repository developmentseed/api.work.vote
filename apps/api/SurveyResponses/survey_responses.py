from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jurisdiction.models import State, Jurisdiction
from .check_authorization import checkAuth
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime

import json

def update_db_responses(answer_dict, jurisdiction_id):
    updated = False
    j = Jurisdiction.objects.get(pk=jurisdiction_id)

    compensation_text = [False, '', '']

    for q, a in answer_dict.items():
        try:
            q_list = q[1:].split(')')
            q_no = int(q_list[0])
            # Sanitize input
            a = str(a)
        except ValueError: # not a question
            # If the key doesn't start with a number, then it's not a question
            continue
        
        if a != "Not Answered" and a != "N/A" and a != "":
            updated = True
            j.display = 'Y'
            if q_no == 1:
                j.website = a
            elif q_no == 2:
                j.application = a
            elif q_no == 3:
                j.telephone = a
            elif q_no == 4:
                j.email = a
            elif q_no == 5:
                j.office_address = a
            elif q_no == 6:
                j.mailing_address = a
            elif q_no == 7:
                j.hours_start = a
            elif q_no == 8:
                j.hours_end = a
            elif q_no == 9:
                j.full_day_req = a[0]
            elif q_no == 10:
                compensation_text[0] = True
                q_list = q.split()
                if q_list[-2] == "Low":
                    compensation_text[1] = '${:,.2f}'.format(float(a))
                elif q_list[-2] == "Upper":
                    compensation_text[2] = '${:,.2f}'.format(float(a))
            elif q_no == 11:
                j.minimum_age = a
            elif q_no == 12:
                j.student_website = a
            elif q_no == 13:
                j.pre_registration = a[0]
            elif q_no == 14:
                # Should change this question
                if a[:3] == "Yes":
                    j.registration_status = "J"
                elif a.strip() == 'No, they just need to be registered to vote in the state.':
                    j.registration_status = "S"
                else: #no registration necessary
                    j.registration_status = "N"
            elif q_no == 15:
                j.must_have_email = a[0]
            elif q_no == 16:
                j.interview = a[0]
            elif q_no == 17:
                # Is this an Other, please specify response
                if "specify" in q_list[1]: 
                    j.training_note = a
                # In the case of a "Yes/No" answer
                else:
                    j.training = a[0]
            elif q_no == 18:
                j.complete_training = a[0]
            elif q_no == 19:
                j.further_notes = a
        else:
            continue
    
    if compensation_text[0] == True:
        if compensation_text[1] != '' and compensation_text[2] != '':
            j.compensation = compensation_text[1] + " to " + compensation_text[2]
        elif compensation_text[1] != '':
            j.compensation = compensation_text[1]
        else:
            j.compensation = compensation_text[2]
    
    if updated:
        j.obtained_at = datetime.today().strftime('%Y-%m-%d')
        j.save()
    
    return updated, [j.name, j.state]


def send_error_email(juris_no, juris_info):
    # Send an email to admin
    send_mail(
        'WorkElections.com: Error on survey response import',
        'No data could be updated from the last survey response for Jurisdiction {}: {}, {}. Check whether the survey format has been changed.'.format(juris_no, juris_info[0], juris_info[1]),
        'info@workelections.com',
        [settings.CONTACT_US],
    )

@csrf_exempt
def GetSurveyResponse(request):
    # check authorization
    try:
        assert checkAuth(request)
    except:
        response = HttpResponse()
        response.status_code = 401
        return response

    decoded = request.body.decode('utf-8')
    try:
        json_dict = json.loads(decoded)
    except json.decoder.JSONDecodeError:
        return HttpResponse(status=400)
    
    # Find jurisdiction to update
    jurisdiction_id = json_dict["Custom Variable__JurisdictionNo"]
    status, juris_info = update_db_responses(json_dict, jurisdiction_id)

    if status:
        return HttpResponse(status=200)
    else: # There was nothing to update
        # should eventually send name and state of jurisdiction
        send_error_email(jurisdiction_id, juris_info)
        return HttpResponse(status=400)
