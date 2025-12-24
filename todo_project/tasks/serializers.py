from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "category",
            "priority",
            "task_date",
            "start_time",
            "end_time",
            "completed",
            "created_at",
        ]
        read_only_fields = ["id", "completed", "created_at"]
