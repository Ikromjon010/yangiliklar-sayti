from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, LogoutView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .views import profile_view, SignUpView2, admin_page_view, EditUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login' ),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('signup/', SignUpView2.as_view(), name='user_register'),

    path('admin-page/', admin_page_view, name='admin_page'),

    # path('profile/edit/', edit_user, name='edit_user_information' ),
    path('profile/edit/', EditUserView.as_view(), name='edit_user_information'),

    path('user-profile/', profile_view, name="user_profile"),
]
