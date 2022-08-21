from django.conf import settings
from celery import shared_task
from django_celery.celery import app
from core.models import TaskBackup


@app.task(bind=True)
def multiply_task(self):
    """ test task """

    from core.libs.multiplication import Multiplication

    return Multiplication.calculate_result()


@app.task(bind=True)
def repeat_multiply_task(self):
    """ run task n times """

    for i in range(100):
        multiply_task.delay()

    return i
