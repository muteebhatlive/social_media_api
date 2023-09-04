from django.urls import path
from .views import user_registration, user_login, user_logout, unfollow_user,follow_user

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('follow_user/', follow_user, name='follow_user'),
    path('unfollow_user/', unfollow_user, name='unfollow_user'),

    
    ]
