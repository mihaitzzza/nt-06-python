from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_admin'


class MyAdminSiteConfig(AdminConfig):
    default_site = 'my_admin.admin.MyAdminSite'
