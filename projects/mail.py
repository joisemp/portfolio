from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading
from django.conf import settings


# Email Thread to speed up submission
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class ContactEmail:

    def __init__(self, full_name, sender_email_id, subject, message):
        self.full_name = full_name
        self.sender_email_id = sender_email_id
        self.subject = subject
        self.message = message

    # Send email to admin on contact form submission
    def send_to_admin(self):
        print("mail send")
        html_content = render_to_string('send_to_admin.html', {
                                        'full_name': self.full_name, 'subject': self.subject, 'message': self.message, 'email': self.sender_email_id, })
        text_content = strip_tags(html_content)
        recipients = [settings.EMAIL_HOST_USER, ]
        from_email = settings.EMAIL_HOST_USER
        email = EmailMultiAlternatives(
            self.subject,
            text_content,
            from_email,
            recipients
        )
        email.attach_alternative(html_content, 'text/html')
        EmailThread(email).start()