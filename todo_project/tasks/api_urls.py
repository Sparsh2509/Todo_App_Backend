from django.urls import path
from .api_views import api_signup , api_login

urlpatterns = [
    path("signup/", api_signup),
    path("login/", api_login),
]
