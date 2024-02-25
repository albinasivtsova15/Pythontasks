Задание 10 Дан список строк с клавиатуры. Упорядочить по количеству
слов в строке.

def sort_by_word(strings1):
    strings1.sort(key=lambda x: len(x.split()))
    return strings

count = int(input("Введите количество строк: "))
strings = []
for i in range(count):
    string = input("Введите строку: ")
    strings.append(string)

sort_strings = sort_by_word(strings)

print("Отсортированный список строк по количеству слов в строке:")
for string in sort_strings:
    print(string)
