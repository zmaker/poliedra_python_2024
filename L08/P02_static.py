class Widget():
    
    #variabile statica
    counter = 0
    
    def __init__(self):
        Widget.counter += 1
        self.var = Widget.counter
        
obj1 = Widget()
print("o1:", obj1.var)

obj2 = Widget()
print("o2:", obj2.var)

obj3 = Widget()
print("o3:", obj3.var)
