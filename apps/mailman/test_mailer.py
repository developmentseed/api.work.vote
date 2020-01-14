from django.core import mail
from django.test import TestCase
from jurisdiction.models import Jurisdiction, State
from mailman import mailer

class MailMakerTestCase(TestCase):
    global test_jurisdiction
    test_jurisdiction = Jurisdiction(email='admin@jurisdiction.com')

    # Tests basic mail sending, and if the reply-to is left as None
    def test_email(self):
        mail_maker = mailer.MailMaker(
            test_jurisdiction,
            subject='Test application subject',
        )

        self.assertEqual(len(mail.outbox), 0)
        mail_maker.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [test_jurisdiction.email])
        self.assertEqual(mail.outbox[0].reply_to, [])

    # Tests that reply-to is set correctly
    def test_email_replyto(self):
        mail_maker = mailer.MailMaker(
            test_jurisdiction,
            subject='Test application subject',
            reply_to=['admin@test.com']
        )

        self.assertEqual(len(mail.outbox), 0)
        mail_maker.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [test_jurisdiction.email])
        self.assertEqual(mail.outbox[0].reply_to, ['admin@test.com'])

class MailSurveyTestCase(TestCase):
    global test_jurisdiction1
    test_state1 = State('New York')
    test_jurisdiction1 = Jurisdiction(name='manhattan', state=test_state1, email='admin1@jurisdiction.com')
    global test_jurisdiction2
    test_state2 = State('California')
    test_jurisdiction2 = Jurisdiction(name='brooklyn', state=test_state2, email='admin2@jurisdiction.com')
    global test_recipients
    test_recipients = ['recipient1', 'recipient2']
    global test_emailtext
    test_emailtext = 'Ipsum Lorem and your basic stuff'

    # Tests that mail survey works if reply-to is filled out
    def test_survey_replyto(self):
        mail_maker = mailer.MailSurvey(
            [['manhattan', test_jurisdiction1], ['brooklyn', test_jurisdiction2]],
            test_recipients,
            test_emailtext,
            subject='Test application subject',
            reply_to=['replyto@here.com']
        )

        self.assertEqual(len(mail.outbox), 0)
        mail_maker.send()
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].to, ['recipient1'])
        self.assertEqual(mail.outbox[1].to, ['recipient2'])
        self.assertEqual(mail.outbox[0].reply_to, ['replyto@here.com'])