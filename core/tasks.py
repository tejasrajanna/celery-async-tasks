from django.conf import settings
from celery import shared_task
from django_celery.celery import app
from core.models import TaskBackup
from datetime import datetime


@app.task(bind=True)
def multiply_task(self, task_model):
    """ test task """

    from core.libs.multiplication import Multiplication

    return Multiplication.calculate_result(task_model)


@app.task(bind=True)
def repeat_multiply_task(self):
    """ run task n times """

    for i in range(100):
        results_db = TaskBackup(
            task_name = "multiply_task", 
            enqueued_at = datetime.now(),
        )
        
        multiply_task.delay(results_db)

    return i
