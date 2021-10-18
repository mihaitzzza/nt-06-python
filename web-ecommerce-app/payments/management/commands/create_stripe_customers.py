from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from payments.models import StripeCustomer
from payments.utils import create_stripe_customer_model

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        users_without_stripe = AuthUserModel.objects.filter(stripe_customer=None)

        for user in users_without_stripe:
            create_stripe_customer_model(user)
