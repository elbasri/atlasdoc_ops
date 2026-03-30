# task_envelope.py

class TaskEnvelope:
    def __init__(self, task_id: str, payload: dict):
        self.task_id = task_id
        self.payload = payload
