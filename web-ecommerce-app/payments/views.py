import json
import stripe
from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from payments.models import StripeCard, Order
from payments.utils import get_user_payment_methods_details
from products.forms import SelectCardForm
from utils.cart import Cart


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


@login_required
def order(request):
    if request.method == 'POST':
        select_card_form = SelectCardForm(request.user, data=request.POST)

        if select_card_form.is_valid():
            # create PaymentIntent
            stripe_card = select_card_form.cleaned_data.get('card')

            cart = Cart(request)
            db_order, order_amount = cart.create_order()
            return_url = f'{settings.LOCALHOST_DOMAIN}{reverse("payments:process")}'

            payment_intent = stripe.PaymentIntent.create(
                amount=int(order_amount * 100),
                currency="ron",
                payment_method_types=["card"],
                payment_method=stripe_card.stripe_id,
                confirm=True,
                return_url=return_url,
                customer=request.user.stripe_customer.stripe_id,
                description=json.dumps({
                    'order': {
                        'id': db_order.id
                    },
                }),
                api_key=settings.STRIPE_SECRET_KEY,
            )

            next_action = payment_intent.get('next_action', {})
            if 'redirect_to_url' in next_action and 'url' in next_action['redirect_to_url']:
                return redirect(next_action['redirect_to_url']['url'])

            return f"{redirect(reverse('payments:process'))}?payment_intent={payment_intent['id']}"

        return redirect(reverse('products:checkout'))

    raise Http404('Method not allowed!')


def process(request):
    if 'payment_intent' in request.GET:
        payment_intent = stripe.PaymentIntent.retrieve(
            request.GET['payment_intent'],
            api_key=settings.STRIPE_SECRET_KEY
        )

        if payment_intent['last_payment_error'] is None:
            return redirect(reverse('payments:succeeded'))

        print("payment_intent['last_payment_error']", payment_intent['last_payment_error'])
        return redirect(reverse('payments:failed'))

    raise Http404('Method not allowed!')


def handle_succeeded_payment(request):
    return HttpResponse('Payment succeeded.')


def handle_failed_payment(request):
    return HttpResponse('Payment failed.')


@login_required
def show_orders(request):
    orders = request.user.orders.all()

    return render(request, 'payments/orders.html', {
        'orders': orders,
    })


@login_required
def show_order_details(request, order_id):
    db_order = get_object_or_404(Order, pk=order_id)

    if db_order.user.id != request.user.id:
        raise Http404('Order not available.')

    return render(request, 'payments/order_details.html', {
        'order': db_order,
    })