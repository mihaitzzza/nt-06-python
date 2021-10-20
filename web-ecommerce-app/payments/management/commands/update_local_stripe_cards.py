import stripe
from django.core.management.base import BaseCommand
from django.conf import settings
from payments.models import StripeCard
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        cards = StripeCard.objects.filter((Q(last4=None) | Q(exp_month=None) | Q(exp_year=None)))

        for card in cards:
            stripe_card_data = stripe.Customer.retrieve_source(
                card.stripe_customer.stripe_id,
                card.stripe_id,
                api_key=settings.STRIPE_SECRET_KEY,
            )

            if card.last4 is None:
                card.last4 = stripe_card_data['last4']

            if card.exp_month is None:
                card.exp_month = stripe_card_data['exp_month']

            if card.exp_year is None:
                card.exp_year = stripe_card_data['exp_year']

            card.save()
