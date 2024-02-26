#Дан целочисленный массив и интервал a..b. Необходимо найти
количество минимальных элементов в этом интервале.

def count_min_elements(arr, a, b):
    count = 0
    arr2 =[]
    for j in arr:
        if a <= j <= b:
            arr2.append(j)
            m = min(arr2)
    for i in arr2:
        if i == m:
            count += 1
    return count

arr = [5, 7, 1, 2, 5, 3, 8, 1, 10, 5, 9, 5]
a = 4
b = 9
print(count_min_elements(arr, a, b))
