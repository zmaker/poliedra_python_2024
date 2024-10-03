s = {'a', 'b', 'c', 'd'}
print(s)

s = {'a', 'b', 'c', 'd', 'b'}
print(s)

l = [1,2,3,4,5,6, 2,3]
s2 = set(l)
print(s2)

s2.add(9)
print(s2)
s2.add(9)
print(s2)

s2.discard(9)
print(s2)
s2.discard(9)

s2.remove(1)
print(s2)

s2.clear()
print(s2)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = A.union(B)
print(C)

D = A.intersection(B)
print(D)

E = A.difference(B)
print(E)
F = B.difference(A)
print(F)

G = A.symmetric_difference(B)
print(G)

print(3 in A)

for el in A:
    print (el, end = ' ')
print("\n")

for el in set("apple"):
    print (el, end = ' ')
print("\n")    
