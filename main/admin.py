from django.contrib import admin

from .models import Task, Status, Reminder


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "executor", "supervisor",
                    "status", "start_time", "planned_time")
    ordering = ("-id", )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("task", "previous_status", "next_status",)
    ordering = ("-id", )


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("task", "content", "users",)
    ordering = ("-id", )
