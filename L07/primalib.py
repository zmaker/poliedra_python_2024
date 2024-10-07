'''
Modulo con funzioni di servizio
Creato il: 07/10/2024
Autore: Mario Rossi
'''

# funzione per salutare
def hello():
    print("ciao!")

# funzione per saluti personalizzati
def salutoConNome(nome):
    print("ciao", nome)

#somma di due numeri
def somma(a, b):
    return a + b

def diff(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 0
    else:
        return a/b

if __name__ == '__main__':
    print("Modulo non eseguibile")