from core.models import TaskBackup
import json
import random
from datetime import datetime

class Multiplication:

    @classmethod
    def calculate_result(cls, task_model):

        task_model.received_at = datetime.now()
        r1 = random.randint(0, 100) 
        r2 = random.randint(100, 200)
        result = r1 * r2
        task_model.task_results = json.dumps([r1, r2, result])

        for i in range(1000000):
            pass

        task_model.successful_at = datetime.now()
        # results_db = TaskBackup(
        #     task_name = "multiply_task", 
        #     task_results = json.dumps([r1, r2, result]),
        #     successful_at= datetime.now()
        # )
        task_model.save()
        return r1, r2, result
        