f = open("dati.txt")
print(f.read())
f.seek(0)
print(f.read())
f.seek(2)
print(f.read())
f.seek(0)

print("\nleggo una linea")
line = f.readline()
print("l1:", line, end='')
line = f.readline()
print("l2:", line)

#riavvolgo il file
f.seek(0)

print("\nstampo tutte le righe una alla volta")
i = 1
for l in f:
    print(i, l, end='')
    i += 1
f.close()