from django.urls import path, include
from users.views import login_user, register_user, logout_user, show_profile, activate, regenerate_token

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', show_profile, name='profile'),
    path('activate/<str:token>/', activate, name='activate'),
    path('regenerate_token/<str:token>/', regenerate_token, name='regenerate_token'),
    path('social-auth/', include('social_django.urls')),
]
