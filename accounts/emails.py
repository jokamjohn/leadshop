from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage

from accounts.tokens import account_activation_token


def send_user_registration_activation_email(request, user, email):
    """
    Send an account activation email to the newly signed up user
    :param email:
    :param request:
    :param user:
    :return:
    """
    mail_subject = 'Activate your Lead Shop account.'
    current_site = get_current_site(request)
    message = render_to_string('accounts/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    email = EmailMessage(mail_subject, message, to=[email])
    email.send()
