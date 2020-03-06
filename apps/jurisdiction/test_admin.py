from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.core import mail
from django.core.urlresolvers import reverse
from jurisdiction.models import Jurisdiction, State, SurveyEmail


class JurisdictionAdminTestCase(TestCase):

  def setUp(self):
    User.objects.create_superuser('admin', 'admin@api.work.vote', 'passwd')
    self.client = Client()
    self.assertTrue(self.client.login(username='admin', password='passwd'))

  def test_fields(self):
    ca = State.objects.create(name='California')
    sf = Jurisdiction.objects.create(name='San Francisco', state=ca)
    url = reverse('admin:jurisdiction_jurisdiction_change', args=(sf.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Jurisdiction Name:')
    self.assertNotContains(response, 'candidate_prohibition')

  def test_csv(self):
    ca = State.objects.create(name='California')
    sm = Jurisdiction.objects.create(name='San Mateo', state=ca)
    sf = Jurisdiction.objects.create(name='San Francisco', state=ca)
    survey_email = SurveyEmail.objects.create(name='Test email')
    survey_email.jurisdiction.add(sm, sf)
    url = reverse('admin:jurisdiction_surveyemail_changelist')
    data = {'action': 'get_csv_survey_links',
            '_selected_action': [survey_email.id]}
    survey_url = 'http://surveymonkey.com/{}'
    with self.settings(SURVEY_MONKEY_URL=survey_url):
      response = self.client.post(url, data)

    # Response has jurisdictions sorted by name.
    self.assertEqual(response.status_code, 200)
    sf_url = survey_url.format(sf.id)
    sm_url = survey_url.format(sm.id)
    self.assertContains(
        response, 'San Francisco,%s\nSan Mateo,%s\n' % (sf_url, sm_url))

  def test_send_multirecipient_email(self):
    ca = State.objects.create(name='California')
    sf = Jurisdiction.objects.create(name='San Francisco', state=ca)

    survey_email = SurveyEmail.objects.create(
        name='Test email',
        recipients='recipient1@state.notreal, recipient2@state.notreal')
    survey_email.jurisdiction.add(sf)
    url = reverse('admin:jurisdiction_surveyemail_changelist')
    data = {'action': 'send_email',
            '_selected_action': [survey_email.id]}
    response = self.client.post(url, data)

    # Response is expected to redirect us back to changelist view.
    self.assertEqual(response.status_code, 302)

    self.assertEqual(len(mail.outbox), 2)
    self.assertEqual(mail.outbox[0].to, ['recipient1@state.notreal'])
    self.assertEqual(mail.outbox[1].to, ['recipient2@state.notreal'])
