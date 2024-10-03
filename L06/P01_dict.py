listino = { 12:"mele", 23:"pere", 34:"kiwi"}
print(listino)

d1 = dict()

print(listino[23])
print(listino.get(23))

listino[34] = 'fragole'
print(listino)

listino[95] = 'kiwi'
print(listino)

print(listino.keys())
for ky in listino.keys():
    print(listino[ky], end = ' ')
print(" ")

for val in listino.values():
    print(val, end = ' ')
print(" ")

print(23 in listino)

listino.pop(34) #chiave
print(listino)

listino.clear()
print(listino)

d1 = {1:'uno', 2:"due", 3:"tre"}
d2 = d1
print("d1", d1)
print("d2", d2)
d1[1] = 'one'
print("d1", d1)
print("d2", d2)

d3 = d1.copy()
print("d3", d3)
d3[2] = 'two'
print("d1", d1)
print("d3", d3)

d4 = dict(d1)


