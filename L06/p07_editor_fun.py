testo = []

def getinfo():
    print("[q] quit | [r] del line | [s] save | [n] new")
    print("[l] load | [a] add line | [h] help | [p] print")

getinfo()

while True:
    cmd = input(">")
    if cmd == 'q':
        print("bye!")
        break
    
    elif cmd == 'h':        
        getinfo()
        
    elif cmd == 'a':
        line = input("<")
        testo.append(line)
        
    elif cmd == 'r':
        ans = input("che riga elimino ?")
        nr = int(ans) - 1
        if (nr >= 0) and (nr < len(testo)):            
            testo.pop(nr)
        else:
            print("riga non valida")
        
    elif cmd == 'l':
        f = open("doc1.txt")
        testo = []
        for l in f:            
            testo.append(l[:-1])
        f.close()
    
    elif cmd == 's':
        f = open("doc1.txt", "w")
        for l in testo:
            f.write(l)
            f.write("\n")
        f.close()
        
    elif cmd == 'p':
        i = 1
        for l in testo:
            print(i, l)
            i += 1
    
    elif cmd == 'n':
        testo = []
        
    else:
        print("?")
    
