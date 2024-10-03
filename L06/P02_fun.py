def saluto_semplice():
    print("hello!")
    
def saluto_personale(nome):
    print("ciao", nome)
    
def somma(a, b):
    s = a + b
    return s

saluto_semplice()
saluto_personale('mario')

n = 'luigi'
saluto_personale(n)

x = somma(12, 23)
print(x)

print(1,2,3,4,5,6)

def amici(*nomi):
    #print(nomi)
    n = len(nomi)
    for nn in nomi:
        print(nn, end=' ')
    print(" ")

amici('mario', 'luigi', 'anna')

def controllo_auto(marcia, velocita, direzione):
    print("marcia:", marcia)
    print("vel:   ", velocita)
    print("dir:   ", direzione)
    

controllo_auto(3, 80, 'N')
controllo_auto(direzione='N', velocita=75, marcia=4)

def saluto_personale2(nome="John"):
    print("ciao", nome)

saluto_personale2()
saluto_personale2("fabio")
    
def calc(a, b):
    p = a * b
    s = a + b
    d = a - b
    return p, s, d

ret = calc(12, 23)
print (ret)

a,b,c = calc(12, 23)
print("prod:", a)
print("somma:", b)
print("sottr:", c)
    