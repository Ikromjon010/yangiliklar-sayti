from django.contrib.auth.views import LoginView
from django.urls import path, include

from .views import profile_view

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login' ),


    path('user-profile/', profile_view, name="user_profile"),


]
