# worker.py

def process_task(task_envelope: dict) -> None:
    """
    Processes a given task envelope.

    Args:
        task_envelope (dict): A dictionary containing task details.
    """
    print(f'Processing task: {task_envelope}')
