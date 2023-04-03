from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.

class StatusChoices(models.TextChoices):
    to_do = 'TD', 'To do'
    in_progress = 'IP', 'In progress'
    finished = 'FI', 'Finished'


class Task(models.Model):
    title = models.CharField(max_length=63, null=True)
    description = models.CharField(max_length=255, null=True)
    executor = models.CharField(max_length=31)
    supervisor = models.CharField(max_length=31)
    status = models.CharField(max_length=2, choices=StatusChoices.choices, default=StatusChoices.to_do)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    planned_time = models.DateTimeField(null=True)


class Reminder(models.Model):
    task = models.ForeignKey(to=Task, on_delete=models.SET_NULL,
                             verbose_name=_("Напоминание"), related_name="reminders",
                             null=True)
    content = models.CharField(max_length=255)
    users = models.CharField(max_length=255)


class Status(models.Model):
    task = models.OneToOneField(to=Task, on_delete=models.SET_NULL,
                                verbose_name=_("Изменение статуса"), related_name="statuses",
                                null=True)
    previous_status = models.CharField(max_length=2, choices=StatusChoices.choices)
    next_status = models.CharField(max_length=2, choices=StatusChoices.choices)
    changed_by = models.CharField(max_length=31)