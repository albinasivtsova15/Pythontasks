Функция 1 Найти количество четных чисел, не взаимно простых с
данным.

def nod(a, b):
    while b:
        a , b = b , a % b
    return a

def ne_mutuall_simple(x):
    #d=[]
    d=0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if nod(x[i], x[j]) !=1  and x[i] % 2== 0 and x[j] %2 == 0:
              #  d.append((x[i],x[j]))
            d=d+2
  return d

a= [8 ,6, 140 ,94, 67, 45]
print(ne_mutuall_simple(a))
