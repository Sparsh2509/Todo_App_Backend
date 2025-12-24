from django.urls import path
from .api_views import api_signup , api_login , api_create_task

urlpatterns = [
    path("signup/", api_signup),
    path("login/", api_login),
    path("tasks/", api_create_task)
]
