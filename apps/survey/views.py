from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route

from django.conf import settings
from django.core.mail import send_mail

from survey.models import Application
from jurisdiction.models import Jurisdiction


class ContactViewSet(viewsets.ViewSet):
    """
    Handle calls coming in from IronWorker
    """

    permission_classes = (AllowAny,)

    @list_route(methods=['post'])
    def us(self, request):
        # Make sure we have the parameters we need
        data = request.data

        if 'name' in data or 'email' in data or 'comment' in data:

            # Send an email to admin
            msg = 'Message received from: %s \n\n' % data.get('name', 'N/A')
            msg = msg + 'Email Address: %s \n\n' % data.get('email', 'N/A')
            msg = msg + 'Message: \n\n'
            msg = msg + data.get('comment', 'Not provided')
            send_mail(
                'New message from contact us page of workelections.com',
                msg,
                'info@workelections.com',
                [settings.CONTACT_US],
                fail_silently=False
            )

            return Response({'detail': 'Thank you.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Nothing was sent'}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def survey(self, request):
        # Make sure we have the parameters we need
        data = request.data

        required_fields = [
            'jurisdiction_id',
            'first_name',
            'last_name',
            'city',
            'county',
            'email',
            'phone',
            'age',
            'languages',
            'technology'
        ]

        age_range = {
            0: '16 to 18',
            1: '19 to 25',
            2: '26 to 35',
            3: '36 to 50',
            4: '51 to 64',
            5: '65 and older'
        }

        missing = []
        for field in required_fields:
            if field not in data:
                missing.append(field)

        if missing:
            return Response({'detail': 'Missing fields: %s' % ', '.join(missing)}, status=status.HTTP_400_BAD_REQUEST)

        # make sure age and technology has a correct value
        try:
            age = age_range[int(data.get('age'))]
            technology = int(data.get('technology'))
        except (TypeError, ValueError):
            return Response({'detail': 'Incorrect value for age or technology'}, status=status.HTTP_400_BAD_REQUEST)

        # make sure languages is a list
        if not isinstance(data.get('languages'), list):
            return Response({'detail': 'Languages field must be a list'}, status=status.HTTP_400_BAD_REQUEST)

        # get jurisdiction
        try:
            jurisdiction = Jurisdiction.objects.get(pk=int(data.get('jurisdiction_id')))
        except (Jurisdiction.DoesNotExist, KeyError, ValueError):
            return Response({'detail': 'Jurisdiction was not found!'}, status=status.HTTP_400_BAD_REQUEST)

        if jurisdiction.application:
            return Response({'detail': 'This jurisdiction supports online application'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not jurisdiction.email:
            return Response({'detail': 'There is no email on file for the jurisdiction'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Send an email to admin
        msg = 'We have received the following applicaiton for Arlington County. \n\n'
        msg = msg + 'First Name: %s \n\n' % data.get('first_name', 'N/A')
        msg = msg + 'Last Name: %s \n\n' % data.get('last_name', 'N/A')
        msg = msg + 'City: %s \n\n' % data.get('city', 'N/A')
        msg = msg + 'County: %s \n\n' % data.get('county', 'N/A')
        msg = msg + 'State: %s \n\n' % 'Virginia'
        msg = msg + 'Email: %s \n\n' % data.get('email', 'N/A')
        msg = msg + 'Phone: %s \n\n' % data.get('phone', 'N/A')
        msg = msg + 'What is your age?: \n %s \n\n' % age
        msg = msg + 'What languages do you speak other than English?: \n %s \n\n' % ", ".join(data.get('languages',
                                                                                                       []))
        msg = msg + ('How familiar are you with working with computer technology on a scale of 1 to 10?' +
                     ' 1 being "not familiar at all" and 10 being "extremely familiar."\n')
        msg = msg + '%s \n\n' % technology
        send_mail(
            '[workelections.com] Poll Worker Request',
            msg,
            'info@workelections.com',
            [settings.CONTACT_US],
            fail_silently=False
        )

        Application.objects.create(
            jurisdiction=jurisdiction,
            city=data.get('city'),
            county=data.get('county'),
            age_range=int(data.get('age')),
            languages=data.get('languages'),
            familiarity_w_technology=technology
        )

        return Response({'detail': 'Thank you.'}, status=status.HTTP_200_OK)
