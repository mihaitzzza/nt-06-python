import stripe
from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from payments.models import StripeCard
from payments.utils import get_user_payment_methods_details


@login_required
def add_card(request):
    if request.method == 'POST':
        if 'stripeToken' not in request.POST:
            raise Http404('Method not allowed')

        stripe_token = request.POST['stripeToken']
        stripe_customer_id = request.user.stripe_customer.stripe_id

        card = stripe.Customer.create_source(
            stripe_customer_id,
            source=stripe_token,
            api_key=settings.STRIPE_SECRET_KEY,
        )

        StripeCard.objects.create(
            stripe_customer=request.user.stripe_customer,
            stripe_id=card['id'],
            last4=card['last4'],
            exp_month=card['exp_month'],
            exp_year=card['exp_year'],
        )

        return redirect(reverse('payments:cards'))

    return render(request, 'payments/add_card.html', {
        'stripe_key': settings.STRIPE_PUBLIC_KEY
    })


@login_required
def show_cards(request):
    cards = get_user_payment_methods_details(request.user)

    return render(request, 'payments/cards.html', {
        'cards': cards,
    })


@login_required
def delete_card(request, card_id):
    card = get_object_or_404(StripeCard, pk=card_id)

    if card.stripe_customer.user.id != request.user.id:
        raise Http404('Card was not found.')

    stripe.Customer.delete_source(
        card.stripe_customer.stripe_id,
        card.stripe_id,
        api_key=settings.STRIPE_SECRET_KEY,
    )

    card.delete()

    return redirect(reverse('payments:cards'))
