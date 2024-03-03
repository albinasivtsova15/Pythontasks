#46 Дан целочисленный массив. Необходимо вывести вначале его
положительные элементы, а затем – отрицательные.

def separate_pol_ot(arr):
    pol = [num for num in arr if num > 0]
    ot = [num for num in arr if num < 0]


    print("Положительные элементы:", pol)
    print("Отрицательные элементы:", ot)


# Пример использования
array = [6, -10, 5, -1, 0, -9]
separate_pol_ot(array)
