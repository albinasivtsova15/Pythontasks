#Функция 3 Найти произведение максимального числа, не взаимно
простого с данным, не делящегося на наименьший делитель исходно числа, и
суммы цифр числа, меньших 5

def find_special_product(arr):
    max_num = max(arr)
    not_coprime = [num for num in arr if num != 1 and num % 2 != 0]
    not_divisible = [num for num in arr if num % 2 != 0 and num % 3 != 0 and num % 5 != 0]
    sum_less_than_5 = sum([int(digit) for num in arr for digit in str(num) if int(digit) < 5])

    special_product = max_num
    for num in not_coprime:
        if num > special_product:
            special_product = num

    for num in not_divisible:
        if num > special_product:
            special_product = num

    special_product *= sum_less_than_5

    return special_product

arr = [12, 7, 9, 15, 4, 6]
result = find_special_product(arr)
print(result)
