from django.urls import path
from payments.views import (
    add_card, show_cards, delete_card, order, process, handle_succeeded_payment, handle_failed_payment,
    show_orders, show_order_details
)

app_name = 'payments'

urlpatterns = [
    path('add-card/', add_card, name='add_card'),
    path('cards/', show_cards, name='cards'),
    path('delete_card/<int:card_id>/', delete_card, name='delete_card'),
    path('order/', order, name='order'),
    path('process/', process, name='process'),
    path('succeeded/', handle_succeeded_payment, name='succeeded'),
    path('failed/', handle_failed_payment, name='failed'),
    path('orders/', show_orders, name='orders'),
    path('orders/<int:order_id>/', show_order_details, name='order_details'),
]
