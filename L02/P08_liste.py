numeri = [10, 20, 30]
print(numeri)

temp = [12.5, 24.56, 18.33, 45.0]
nomi = ["Mario", "Luigi", "Anna"]
cose_varie = ["Mario", "Rossi", 1975, 1.78]

print("elemento con indice 0:", numeri[0])

i = 0
print("elemento con indice", i, ":", numeri[i])
i = 1
print("elemento con indice", i, ":", numeri[i])
i = 2
print("elemento con indice", i, ":", numeri[i])

numeri[2] = 99
print(numeri)

l1 = []
print(l1)
l2 = list()
print(l2)

print("numero di elementi di numeri: ", len(numeri))

l1.append(1)
print("l1", l1)
l1.append(2)
print("l1", l1)
l1.append("gatto")
print("l1", l1)
l1.append("cane")
l1.append("topo")

print("numeri:", numeri)
numeri.insert(1, 123)
print("numeri:", numeri)

numeri.extend([100, 101, 102])
print("numeri:", numeri)

print("l1", l1)
l1.remove("topo")
print("l1", l1)

print("numeri:", numeri)
numeri.pop()
print("numeri:", numeri)
numeri.pop(1)
print("numeri:", numeri)

la = [1,2,1,3,4,5,6,1]
print("la:", la)
la.remove(1)
print("la:", la)

matrice = [[1,2,3],[4,5,6],[7,8,9]]
print(matrice)

print(9 in la)
print(2 in la)


