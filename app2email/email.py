from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_review_email(name, email, review):
    context = {
        'name': name,
        'email': email,
        'review': review,
    }

    email_subject = 'thank you for review'
    email_body = render_to_string('email_msg.txt', context)

    email_final = EmailMessage(
        email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email,],
    )

    return email_final.send(fail_silently=False)