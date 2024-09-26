import random

RIPETI = True

while RIPETI:
    ans = input("estraggo un numero (s/n)? ")
    if ans == 's':
        n = random.randint(1,91)
        print(n)
    else:
        RIPETI = False