from django.urls import path
from stores.views import show_stores, show_details

app_name = 'stores'

urlpatterns = [
    path('', show_stores, name='all'),
    path('<int:id>/', show_details, name='details')
]
