class Led():
    def __init__(self):
        self.i = 0
        self.v = 0
        self.__seriale = 123456
    
    def alimenta(self, corrente=0, tensione=0):
        self.i = corrente
        self.v = tensione
        
    def __str__(self):
        return f"LED: {self.i}@{self.v} ({self.__seriale})"
    
    def getSeriale(self):
        return self.__seriale
    
    def setSeriale(self, n):
        self.__seriale = n
    
l1 = Led()
print(l1)
l1.alimenta(1, 10)
print(l1)
l1.i = 2
print(l1)
l1.setSeriale(555)
print(l1)
print(l1.getSeriale())