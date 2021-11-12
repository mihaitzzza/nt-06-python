from unittest import mock
from django.test import TestCase
from django.contrib.auth import get_user_model
from payments.models import StripeCustomer

AuthUserModel = get_user_model()


class StripeTestCase(TestCase):
    @mock.patch('stripe.Customer.create')
    def test_create_stripe_customer(self, stripe_create_customer_mock):
        stripe_create_customer_mock.return_value = {
            'id': 'mocked_custom_id_1234'
        }

        AuthUserModel.objects.create_user(
            email='a@gmail.com',
            first_name='Mihai',
            last_name='Vladu',
        )

        try:
            StripeCustomer.objects.get(stripe_id='mocked_custom_id_1234')
        except StripeCustomer.DoesNotExist:
            self.fail('Stripe Customer with ID = mocked_custom_id_1234 does not exist.')
