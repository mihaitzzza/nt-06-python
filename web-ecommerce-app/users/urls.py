from django.urls import path
from users.views import login_user, register_user, logout_user, show_profile

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', show_profile, name='profile'),
]
