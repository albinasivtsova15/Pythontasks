Задание 9 Прочитать список строк с клавиатуры. Упорядочить по длине
строки.

n = int(input("Введите количество строк: "))
strings = []
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)

strings.sort(key=len)

print("Отсортированный список строк:")
for string in strings:
    print(string)
