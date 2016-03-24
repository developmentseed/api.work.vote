from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import list_route, permission_classes as pm

from django.conf import settings
from django.core.mail import send_mail

from survey.models import Application, Survey
from mailman.mailer import MailMaker
from api.serializer import add_city_string
from jurisdiction.models import Jurisdiction
from survey.export import export_applications, export_surveys


class ContactViewSet(viewsets.ViewSet):
    """
    Handle calls coming in from IronWorker
    """

    permission_classes = (AllowAny,)

    age_range = {
        0: '16 to 18',
        1: '19 to 25',
        2: '26 to 35',
        3: '36 to 50',
        4: '51 to 64',
        5: '65 and older'
    }

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
            'age',
            'languages',
            'technology'
        ]

        missing = []
        for field in required_fields:
            if field not in data:
                missing.append(field)

        if missing:
            return Response({'detail': 'Missing fields: %s' % ', '.join(missing)}, status=status.HTTP_400_BAD_REQUEST)

        # make sure age and technology has a correct value
        try:
            age_id = int(data.get('age'))
            age = self.age_range[age_id]
        except (TypeError, ValueError):
            age_id = None
            age = None

        try:
            technology = int(data.get('technology'))
        except (TypeError, ValueError):
            technology = 0

        # make sure languages is a list
        if not isinstance(data.get('languages'), list):
            return Response({'detail': 'Languages field must be a list'}, status=status.HTTP_400_BAD_REQUEST)

        Survey.objects.create(
            age_range=age_id,
            languages=data.get('languages'),
            familiarity_w_technology=technology
        )

        return Response({'detail': 'Thank you.'}, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def application(self, request):
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

        missing = []
        for field in required_fields:
            if field not in data:
                missing.append(field)

        if missing:
            return Response({'detail': 'Missing fields: %s' % ', '.join(missing)}, status=status.HTTP_400_BAD_REQUEST)

        # make sure age and technology has a correct value
        try:
            age_id = int(data.get('age'))
            age = self.age_range[age_id]
        except (TypeError, ValueError):
            age_id = None
            age = None

        try:
            technology = int(data.get('technology'))
        except (TypeError, ValueError):
            technology = 0

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

        context = {
            'jurisdiction_name': add_city_string(jurisdiction),
            'first_name': data.get('first_name', None),
            'last_name': data.get('last_name', None),
            'city': data.get('city', None),
            'county': data.get('county', None),
            'email': data.get('email', None),
            'phone': data.get('phone', None),
            'age': age,
            'technology': technology,
            'languages': ', '.join(data.get('languages', []))
        }

        # send email
        mail = MailMaker(jurisdiction, **context)
        mail.send()

        Application.objects.create(
            jurisdiction=jurisdiction,
            city=data.get('city'),
            county=data.get('county'),
            age_range=age_id,
            languages=data.get('languages'),
            familiarity_w_technology=technology
        )

        return Response({'detail': 'Thank you.'}, status=status.HTTP_200_OK)

    @list_route()
    @pm((IsAuthenticated, ))
    def applications_export(self, request):
        return export_applications()

    @list_route()
    @pm((IsAuthenticated, ))
    def surveys_export(self, request):
        return export_surveys()
