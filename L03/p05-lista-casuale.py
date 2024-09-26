import random

numeri = []

for i in range(0,10):
    n = random.randint(0,1000)
    numeri.append(n)
    print(numeri)

print(len(numeri))

for el in numeri:
    print(el, end=' ' )