peso_panino = int(input('peso: '))

if (peso_panino > 200):
    peso_netto = peso_panino - 10
    print("WARN!", peso_netto, "troppe calorie!")
else:
    peso_netto = peso_panino - 8
    print("Ok, il panino va bene!", peso_netto)
    
print("fine programma")
