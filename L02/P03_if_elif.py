txt = input("che voto hai preso? ")
voto = int(txt)

if (voto <= 4):
    print("grav. insuff")
elif (voto == 5):
    print("insuff")
elif (voto == 6):
    print("suff")
elif (voto == 7):
    print("discreto")
elif (voto == 8):
    print("buono")
elif (voto == 9):
    print("ottimo")
elif (voto == 10):
    print("ottimo con lode")
else:
    print("voto non valido!")
