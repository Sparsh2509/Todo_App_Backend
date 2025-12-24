from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", api_signup),
    path("login/", api_login),
    path("tasks/", api_tasks),
    path("tasks/<int:task_id>/delete", api_delete_task),
    path("tasks/<int:task_id>/toggle/", api_toggle_task),
    path("tasks/<int:task_id>/update", api_update_task)

    
]
