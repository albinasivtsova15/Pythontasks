15 Дано натуральное число. Необходимо найти количество различных
цифр в его десятичной записи.

def count_digit_of_number(number):
    digs = set(str(number))
    return len(digs)

num = int(input("Введите натуральное число: "))
r = count_digit_of_number(num)
print("Количество различных цифр в числе", num, ":",  r)
