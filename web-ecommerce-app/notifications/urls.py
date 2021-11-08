from django.urls import path
from notifications.views import show_notifications

app_name = 'notifications'

urlpatterns = [
    path('', show_notifications, name='view_all')
]
