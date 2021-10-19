from django.urls import path
from payments.views import add_card, show_cards

app_name = 'payments'

urlpatterns = [
    path('add-card/', add_card, name='add_card'),
    path('cards/', show_cards, name='cards'),
]
