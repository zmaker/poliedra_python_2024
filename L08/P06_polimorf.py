class Forma():
    def area(self):
        return 0

class Rect(Forma):
    def __init__(self, l, a):
        self.l = l
        self.a = a
        
    def area(self):
        return self.l * self.a
    
class Tri(Forma):
    def __init__(self, b, a):
        self.b = b
        self.a = a
        
    def area(self):
        return (self.b * self.a) / 2

class Cerchio(Forma):
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return (self.r * self.r) * 3.14
    
r = Rect(10, 20)
print("r: ", r.area())

t = Tri(10, 20)
print("t: ", t.area())

c = Cerchio(10)
print("c: ", c.area())


