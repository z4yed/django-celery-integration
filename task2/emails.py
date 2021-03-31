from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(subject, email, review):

    subject = subject

    context = {
        'subject': subject,
        'email': email,
        'review': review,
    }

    email_body = render_to_string('email_body.txt', context)

    send_mail(
        subject,
        email_body,
        EMAIL_HOST_USER, [email]
    )
    return 'Email Sent'
