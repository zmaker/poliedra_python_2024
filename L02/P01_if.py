peso_panino = int(input('peso: '))

if (peso_panino > 200):
    peso_netto = peso_panino - 10
    print("WARN!", peso_netto, "troppe calorie!")    
    
print("fine programma")