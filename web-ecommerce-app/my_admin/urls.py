from django.urls import path
from my_admin.admin import my_admin_site

urlpatterns = [
    path('', my_admin_site.urls)
]
