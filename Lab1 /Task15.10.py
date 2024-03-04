10 Даны два массива. Необходимо найти количество совпадающих по
значению элементов.

def count_elements(arr1, arr2):
    count = 0
    for i in arr1:
        for j in arr2:
            if i == j:
                count += 1
    return count

arr1 = [1, 2, 3, 4, 5, 8, 10, 12]
arr2 = [3, 4, 5, 6, 7, 9, 10, 12, 15]
print( count_elements(arr1, arr2))
