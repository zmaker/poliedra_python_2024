class Led():
    
    def __init__(self, color='green'):
        self.colore = color
        self.stato = 'OFF'
        #variabile non esposta (privata)
        self.__serialnumb = 123456
    
    def __str__(self):
        return f"Led ({self.colore}, {self.stato}) #{self.__serialnumb}"
    
    def accendi(self):
        self.stato = 'ON'
    
    def spegni(self):
        self.stato = 'OFF'
    
    def getStato(self):
        return self.stato
    
    def setColore(self, newcol):
        self.colore = newcol
        
    def __del__(self):
        print("Led distrutto")
        

l1 = Led()
print("1", l1.colore)
print("2", l1)

l1.accendi()
print("3", l1)
print("4", l1.getStato())
l1.spegni()
print("5", l1.getStato())

l1.setColore("blu")
print("6", l1)

#l1.__serialnumb = 0
#print("7", l1.__serialnumb)

l2 = Led('red')
print("8", l2)

del l2
del l1
