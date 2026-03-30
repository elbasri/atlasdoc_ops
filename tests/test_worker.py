# test_worker.py

from src.worker import process_task

def test_process_task():
    task_envelope = {'task_id': '1', 'payload': {'data': 'example'}}
    process_task(task_envelope)
