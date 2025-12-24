from django.urls import path
from .api_views import api_signup , api_login , api_tasks , api_delete_task

urlpatterns = [
    path("signup/", api_signup),
    path("login/", api_login),
    path("tasks/", api_tasks),
    path("tasks/<int:task_id>/", api_delete_task)

]   
