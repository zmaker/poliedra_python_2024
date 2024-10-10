class Rect():
    def __init__(self, h, w):
        self.h = h
        self.w = w
    
    def area(self):
        return self.h * self.w

class Quad(Rect):
    def __init__(self, l):
        super().__init__(l, l)


r = Rect(10,20)
print("Area Rect: ", r.area())

q = Quad(10)
print("Area Quad: ", q.area())