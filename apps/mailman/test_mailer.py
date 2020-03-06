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

    def test_mulitaddress_email(self):
        email1 = 'admin1@jurisdiction.com'
        email2 = 'admin2@jurisdiction.com'
        test_jurisdiction = Jurisdiction(email='%s;%s' % (email1, email2))
        mail_maker = mailer.MailMaker(
            test_jurisdiction,
            subject='Test application subject',
        )
        self.assertEqual(len(mail.outbox), 0)
        mail_maker.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [email1, email2])
