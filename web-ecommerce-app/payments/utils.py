import stripe
from django.conf import settings
from payments.models import StripeCustomer


def create_stripe_customer_model(user_instance):
    stripe_customer = stripe.Customer.create(
        email=user_instance.email,
        name=f'{user_instance.first_name} {user_instance.last_name}',
        api_key=settings.STRIPE_SECRET_KEY
    )

    StripeCustomer.objects.create(user=user_instance, stripe_id=stripe_customer['id'])


def get_user_payment_methods_details(user):
    payment_methods_response = stripe.PaymentMethod.list(
        customer=user.stripe_customer.stripe_id,
        type='card',
        api_key=settings.STRIPE_SECRET_KEY,
    )

    cards = [data['card'] for data in payment_methods_response['data']]

    return cards
