from celery import Celery, group

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

@app.task
def add(numbers):
    return sum(numbers)

@app.task
def process_subtask(numbers):
    result = add.delay(numbers)
    return result.get()

def split_into_subtasks(numbers_list, chunk_size):
    chunks = [numbers_list[i:i + chunk_size] for i in range(0, len(numbers_list), chunk_size)]
    return chunks

@app.task(bind=True)
def parallel_add(self, numbers_list, chunk_size):
    subtask_chunks = split_into_subtasks(numbers_list, chunk_size)

    subtasks = group(process_subtask.s(chunk) for chunk in subtask_chunks)
    results = subtasks.apply_async()
    total_sum = sum(result.get() for result in results.join())

    return total_sum
