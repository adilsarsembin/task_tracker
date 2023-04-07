from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import TaskSerializer, StatusSerializer, ReminderSerializer
from .models import Task, Status, Reminder


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
