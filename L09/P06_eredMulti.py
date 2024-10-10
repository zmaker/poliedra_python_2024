class Forma():
    def __init__(self, l, w):
        self.l = l
        self.w = w

class Colorato():
    def __init__(self, c):
        self.colore = c
    
class Rect(Forma, Colorato):
    def __init__(self, l, w, c):
        Forma.__init__(self, l, w)
        Colorato.__init__(self, c)
        
    def area(self):
        return self.w * self.l
    
    def __str__(self):
        return f"Rect [{self.l}x{self.w}] ({self.colore})"

class Quad(Rect):
    def __init__(self, l, c):
        super().__init__(l,l, c)
    
    def __str__(self):
        return f"Quad [{self.l}x{self.l}] ({self.colore})"

r = Rect(10, 20, "rosso")
print(r, r.area())

q = Quad(10, "blu")
print(q)
