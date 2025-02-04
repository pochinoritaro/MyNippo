from django.contrib.auth.views import LogoutView
from django.urls import path
from account.views import LoginView, ProfileView, SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup")
]
