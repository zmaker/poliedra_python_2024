import random

segreto = random.randint(1,10)
print(segreto)

print("indovina il numero")

n = 0

tentativi = 3
indovinato = False

while not(n == segreto):
    ans = input("che numero? ")
    n = int(ans)
    
    if not(n == segreto):
        indovinato = False
        tentativi -= 1
    else:
        indovinato = True
        
    if tentativi <= 0:
        print("hai terminato i tentativi")
        break
    
if (indovinato):
    print("corretto")
else:
    print("hai perso")
    

