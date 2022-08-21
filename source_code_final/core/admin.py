from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import *

# Register your models here.

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['task_name', 'task_results', 'successful_at']

admin.site.register(TaskBackup, TaskAdmin)
