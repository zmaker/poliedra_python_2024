import os

if os.path.exists("todel.txt"):
    print("lo rimuovo...")
    os.remove("todel.txt")
    print("rimosso")
else:
    print("non trovato: lo creo")
    file = open("todel.txt", "w")
    file.close()

    