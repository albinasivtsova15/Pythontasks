11 Дана строка в которой записаны слова через пробел. Необходимо
посчитать количество слов.

def count_words(x):
    words = x.split()
    return len(words)

a=input()
print(count_words(a))
