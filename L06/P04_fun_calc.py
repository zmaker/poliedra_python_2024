def somma(a,b):
    s = a + b
    return s

def molt(a,b):
    p = a * b
    return p

def div(a,b):
    d = 0
    if not (b == 0):
        d = a / b
    return d

print("calcolatrice")
ans = input("primo numero: ")
a = int(ans)
ans = input("secondo numero: ")
b = int(ans)
op = input("che operazione? [+, x, :] ")

res = 0
if (op == '+'):
    res = somma(a, b)

elif (op == 'x'):
    res = molt(a, b)

elif (op == ':'):
    res = div(a, b)

else:
    res = -1

print("risultato: ", res)