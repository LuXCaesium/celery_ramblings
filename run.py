from tasks import add
from celery import group

result_group = group(add.s(i, i) for i in range(1000))()

result_objects = list(result_group)

processed_tasks = {}

while result_objects:
    for result in result_objects:
        if result.ready() and result.successful():
            df_result = result.get()
            print(df_result)
            processed_tasks[result.id] = df_result
            
    result_objects = [result for result in result_objects if result.id not in processed_tasks]