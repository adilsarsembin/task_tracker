from rest_framework import serializers

from .models import Task, Reminder, Status


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "executor", "supervisor",
                  "status", "start_time", "end_time", "planned_time"]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "previous_status", "next_status", "changed_by"]


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ["id", "content", "users"]
