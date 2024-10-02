lista = [1,2,3]
tupla = (5,6,7)
print("lista", lista, "tupla", tupla)

mix = (1, "ciao", 3.4)

print("\nfor su tupla")
i = 1
for el in mix:
    print(i, ":", el)
    i += 1

print("\nelemento di un tupla:", mix[1])
print("\nn. di elementi di un tupla:", len(mix))

t1 = ('a', 'b', 'c', 'b', 'e')
print("\ncount a:", t1.count('a'))
print("count b:", t1.count('b'))

print("\nestrazione con while")
i = 0
while (i < len(t1)):
    print(i, ":", t1[i])
    i += 1

print("\npack/unpack")
pack = 3, "mele", 1.98
print(pack)

a,b,c = pack
print(a)
print(b)
print(c)

print( "\nb è in t1?", ('b' in t1) )
print( "\nposizione di c:", t1.index('c') )

#non possibile
#t1[2] = 12

print(pack + t1)
print(pack * 3)

    