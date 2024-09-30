testo = []

while (True):
    cmd = input("> ")
    if cmd == 'i':
        #inserisco un testo
        line = input("> ")
        testo.append(line)
    
    elif cmd == 'q':
        #termino
        break
    
    elif cmd == 'p':
        #stampo
        i = 1
        for l in testo:
            print(f"{i}: {l}")
            i += 1

    else:
        print("???")

print("end")