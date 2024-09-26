# lista della spesa per 3 elementi

print("Lista Spesa")

ans = input("Quante cose ti servono? ")
num_elementi = int(ans)

spesa = []

for i in range(0,num_elementi):
    print(f"elemento n.:{(i+1)}" )
    ans = input("cosa ti compro? ")
    spesa.append(ans)

print(f"nella lista ci sono: {len(spesa)} elementi")

input("premi invio")

print("\nla lista comprende:")
pos = 1
for el in spesa:
    print(f"{pos}: {el}")
    pos += 1