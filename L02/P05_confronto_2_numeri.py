print("Confronto tra due numeri")

ans = input("primo numero (solo numeri interi): ")
n1 = int(ans)
ans = input("secondo numero (solo numeri interi): ")
n2 = int(ans)

if (n1 > n2):
    print(n1, ">", n2)
elif (n1 < n2):
    print(n2, ">", n1)
else:
    print("sono uguali")
    