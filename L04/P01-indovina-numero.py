import random

segreto = random.randint(1,10)

print("indovina il numero")

ans = input("che numero? ")
n = int(ans)

while not(n == segreto):
    ans = input("che numero? ")
    n = int(ans)

print("corretto")
    