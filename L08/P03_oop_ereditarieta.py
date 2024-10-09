class Auto():
    def __init__(self, colore, anno):
        self.color = colore
        self.year = anno
        self.speed = 0
    
    def setSpeed(self, s):
        self.speed = s
    
    def beep(self, suono):
        return f"{suono} -)))"
        
    def __str__(self):
        return f"[Auto] c:{self.color} y:{self.year} spd:{self.speed}"

class Fiat500(Auto):
    def beep(self, suono):
        return f"La 500 suona così: {suono}!"
    
class Perrari(Auto):
    def beep(self, suono):
        return f"La Perrari suona così: {suono}!"
    
    def __str__(self):
        return f"[Perrari] c:{self.color} y:{self.year} spd:{self.speed}"

a1 = Auto("rosso", 1999)
a1.setSpeed(10)
print(a1.beep("BI"))
print(a1)

a2 = Fiat500("gialla", 2012)
a2.setSpeed(100)
print(a2.beep("Honk"))
print(a2)

a3 = Perrari("silver", 2021)
print(a3.beep("UUUUU"))
print(a3)

print(isinstance(a3, Perrari))



