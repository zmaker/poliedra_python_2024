print("Confronto tra tre numeri")

ans = input("primo numero (solo numeri interi): ")
a = int(ans)
ans = input("secondo numero (solo numeri interi): ")
b = int(ans)
ans = input("terzo numero (solo numeri interi): ")
c = int(ans)

if (a > b):
    #qui a è maggiore di b, quindi scarto b
    if (a > c):
        print("A", a)
    else:
        print("C", c)
else:
    if (b > c):
        print("B", b)
    else:
        print("C", c)