from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import reverse
from utils.constants.activation import ACTIVATION_UNIT, ACTIVATION_VALUE


def send_activation_mail(activation):
    user = activation.user
    activate_route = reverse('users:activate', args=(activation.token,))

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'unit': ACTIVATION_UNIT,
        'value': ACTIVATION_VALUE,
        'url': f'{settings.LOCALHOST_DOMAIN}{activate_route}'
    }

    template = get_template('users/emails/activation.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='You created a new account',
        body=content,
        to=[user.email],
    )
    mail.content_subtype = 'html'
    mail.send()
