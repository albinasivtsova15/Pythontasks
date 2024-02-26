34 Дан целочисленный массив и отрезок a..b. Необходимо найти
элементы, значение которых принадлежит этому отрезку.

def count_min_elements(arr, a, b):
    count = 0
    arr2 =[]
    for j in arr:
        if a <= j <= b:
            arr2.append(j)
    return arr2

arr = [5, 7, 1, 2, 5, 3, 8, 1, 10, 5, 9, 5]
a = 2
b = 8
print(count_min_elements(arr, a, b))
