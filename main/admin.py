from django.contrib import admin

from .models import Task, Status, Reminder

# Register your models here.

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Reminder)