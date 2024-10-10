class Led():
    def __init__(self):
        self.__temp = 450
        self.__colore = "white"

    @property
    def temperatura(self):
        return self.__temp
    
    @temperatura.setter
    def temperatura(self, t):
        self.__temp = t
        
l1 = Led()
print(l1.temperatura)
l1.temperatura = 555
print(l1.temperatura)