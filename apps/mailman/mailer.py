from django.conf import settings
from django.template.loader import get_template
from django.core.mail import get_connection, EmailMultiAlternatives
from apps.mailman.templates.mailman.survey_email_html import write_button, write_html
from html.parser import HTMLParser


class PlainTextMailConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
        self.current_href = ''
        self.strict = False
        self.convert_charrefs= True

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.current_href = dict(attrs).get('href')
        elif tag == 'br':
            self.fed.append('\n')

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_href:
            self.fed.append(' (%s)' % self.current_href)
            self.current_href = ''
        elif tag == 'p':
            self.fed.append('\n')

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)


def clean_emails(email_string):
    if ',' in email_string:
        emails = email_string.split(',')
    elif '\r\n' in email_string:
        emails = email_string.split('\r\n')
    elif '\n' in email_string:
        emails = email_string.split('\n')
    elif ';' in email_string:
        emails = email_string.split(';')
    else:
        emails = [email_string]  # Assume only one e-mail.

    return [item.strip(' ') for item in emails]


class MailMaker(object):

    def __init__(
        self,
        jurisdiction,
        subject='PollWorker application from workelections.com',
        **kwargs
    ):
        if settings.TEST_TO_EMAIL:
            to_emails = settings.TEST_TO_EMAIL
        else:
            to_emails = jurisdiction.email
        self.to_emails = clean_emails(to_emails)

        self.from_email = settings.DEFAULT_FROM_EMAIL
        self.subject = subject
        self.context = {'jurisdiction': jurisdiction}
        self.context.update(kwargs)
        self.html_template = get_template('mailman/html_template.html')
        self.text_template = get_template('mailman/text_template.txt')

    def send(self):
        text_content = self.text_template.render(self.context)
        html_content = self.html_template.render(self.context)

        msg = EmailMultiAlternatives(self.subject, text_content,
                                     self.from_email, self.to_emails)
        msg.attach_alternative(html_content, "text/html")
        msg.send()


# These two classes could be combined, but for now keep separate
class MailSurvey(object):

    def __init__(
        self,
        jurisdictions,
        recipients,
        email_text,
        subject='WorkElections.com Survey',
        **kwargs
    ):
        self.from_email = settings.DEFAULT_SURVEY_FROM_EMAIL
        self.subject = subject
        self.to_email = recipients
        self.email_text = email_text
        c = PlainTextMailConverter()
        c.feed(email_text)
        self.email_plaintext = c.get_data()

        link_text = ""
        link_html = '\n<table width="100%"><tbody>'
        linecount = 0
        for pair in jurisdictions:
            if linecount % 4 == 0:
                link_html += "<tr>"
            link_html += write_button(settings.SURVEY_MONKEY_URL.format(pair[1]), pair[0])
            if linecount % 4 == 3:
                link_html += "</tr>"
            link_text += pair[0]+ ": " + settings.SURVEY_MONKEY_URL.format(pair[1]) + "\n"
            linecount += 1
        while linecount % 4 != 0:
            link_html += "<td></td>"
            linecount += 1
        link_html += "</tbody></table>"
        self.context={'EmailText': self.email_plaintext, 'SurveyLinkText': link_text}
        self.html = write_html(self.email_text, link_html)
        self.text_template = get_template('mailman/survey_email_text.txt')

    def send(self):
        text_content = self.text_template.render(self.context)
        html_content = self.html

        connection = get_connection()
        messages = []
        for recipient in self.to_email:
            message = EmailMultiAlternatives(self.subject, text_content,
                                             self.from_email, [recipient])
            message.attach_alternative(html_content, "text/html")
            messages.append(message)
        try:
            connection.send_messages(messages)
            return 'OK'
        except:
            return 'ERROR'
