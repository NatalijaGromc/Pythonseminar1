# Найти максимальное из пяти чисел.
arr = [23,12,55,20,58,50250,2020]
max = arr[0]
for i in range(len(arr)):
    if (arr[i] > max):
        max = arr[i]
print(max)