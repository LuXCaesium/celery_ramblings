from tasks import parallel_add

numbers_list = [1, 2, 3, 4, 5]
chunk_size = 2  # Adjust the chunk size as needed

result = parallel_add.delay(numbers_list, chunk_size)
print(result.get())
