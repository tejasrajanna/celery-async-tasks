from django.db import models
from django.contrib import admin

# Create your models here.

class TaskBackup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_length=25)
    task_results = models.TextField()
    successful_at = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.created_at, self.updated_at)
