#58 Для введенного списка вывести количество элементов, которые могут
быть получены как сумма двух любых других элементов списка.

def count_elements_as_sum(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] in arr:
                    count += 1

    return count // 2  



array = [2, 4, 6, 8, 10]
result = count_elements_as_sum(array)
print("Количество элементов, которые могут быть получены как сумма двух других элементов списка:", result)
