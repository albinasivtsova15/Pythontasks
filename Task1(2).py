#Функция 2 Найти количество нечетных цифр числа, больших 3
def maxim(x):
    m=0
    while x != 0:
        b = x % 10
        if b > m:
            m = b
        x//=10
    return m

n=int(input())
print(maxim(n))
