from django.urls import path
from stores.views import show_stores

app_name = 'stores'

urlpatterns = [
    path('', show_stores, name='all'),
]
