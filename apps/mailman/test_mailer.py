from django.core import mail
from django.test import SimpleTestCase
from jurisdiction.models import Jurisdiction
from mailman import mailer

class MailMakerTestCase(SimpleTestCase):

    def test_email(self):
        test_jurisdiction = Jurisdiction(email='admin@jurisdiction.com')
        mail_maker = mailer.MailMaker(
            test_jurisdiction,
            subject='Test application subject',
        )
        self.assertEqual(len(mail.outbox), 0)
        mail_maker.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [test_jurisdiction.email])
