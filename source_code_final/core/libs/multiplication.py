from core.models import TaskBackup
import json
import random
from datetime import datetime

class Multiplication:

    @classmethod
    def calculate_result(cls):
        r1 = random.randint(0, 100) 
        r2 = random.randint(100, 200)
        result = r1 * r2
        results_db = TaskBackup(
            task_name = "multiply_task", 
            task_results = json.dumps([r1, r2, result]),
            successful_at= datetime.now()
        )
        results_db.save()
        return r1, r2, result
        