# https://www.w3schools.com/python/python_strings_methods.asp
msg = 'ciao'
msg2 = "hello"

a = "hello"
b = "world"
c = a + b
print(c)

a = "v: "
n = 10
b = "."
c = a + str(n) + b
print(c)

temperatura = 18.5
print(f"la temp. di oggi è: {temperatura} C")

a = 'helloworld'
print(a[0])
for ch in a:
    print(ch, end="_")
print(" ")

print("la stringa è lunga: ", len(a))

txt = "nel mezzo del cammin di nostra vita"
if "vita" in txt:
    print("trovata")
    
print(txt.upper())

if "vita".upper() in txt.upper():
    print("trovata UPPER")

sub1 = txt[3:8]
print(sub1)
sub1 = txt[:8]
print(sub1)
sub1 = txt[10:]
print(sub1)
sub1 = txt[-2:]
print(sub1)

txt = "  nel mezzo del cammin di nostra vita  "
txt2 = txt.strip()
print(f"#{txt2}#")

print(txt.replace("e", "*"))
print(txt.replace("vita", "gita"))

txt = "12,23,34,45,56,67,78,89"
lista = txt.split(",")
for el in lista:
    print(el, end=" - ")
print(" ")

txt = "nel mezzo/del cammin di"
n = txt.index("/")
print(n)
a = txt[:n]
print(a)





