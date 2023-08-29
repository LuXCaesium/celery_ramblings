from tasks import add

numbers_list = [1, 2, 3, 4, 5]
result = add.delay(numbers_list)
print(result.get())
