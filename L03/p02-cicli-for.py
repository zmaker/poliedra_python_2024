frutta = ['mela', 'pera', 'banana', 'kiwi']

for el in frutta:
    print(el)

print(" ")
pos = 1
for el in frutta:
    print(pos, el)
    pos += 1 #pos = pos + 1

print(" ")
msg = "nel mezzo del cammin di..."
for ch in msg:
    print(ch, end='_')

print("\n ")
for i in range(0, 10):
    print(i, end=' ')
    
print("\n ")
for i in range(0, 10, 2): #terzo parametro: passo
    print(i, end=' ')
    
print("\n ")
