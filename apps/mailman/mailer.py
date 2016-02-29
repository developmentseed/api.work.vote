from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class MailMaker(object):

    def __init__(
        self,
        jurisdiction,
        subject='PollWorker application from workelections.com',
        **kwargs
    ):
        # Make sure email is valid
        if settings.TEST_TO_EMAIL:
            self.to_email = settings.TEST_TO_EMAIL
        else:
            self.to_email = jurisdiction.email
        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.subject = subject
        self.context = {
            'jurisdiction': jurisdiction,
        }

        self.context.update(kwargs)

        self.html_template = get_template('mailman/html_template.html')
        self.text_template = get_template('mailman/text_template.txt')

    def send(self):
        if self.context:
            c = Context(self.context)

        text_content = self.text_template.render(c)
        html_content = self.html_template.render(c)

        msg = EmailMultiAlternatives(self.subject, text_content,
                                     self.from_email, [self.to_email])
        msg.content_subtype = "html"
        msg.attach_alternative(html_content, "text/html")
        msg.send()
