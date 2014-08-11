from django.contrib import admin
from todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'complete', 'created_by', 'created_at']
    ordering = ['name']

admin.site.register(Task, TaskAdmin)