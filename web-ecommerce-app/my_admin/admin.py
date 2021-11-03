from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    login_template = 'my_admin/login.html'


my_admin_site = MyAdminSite()
