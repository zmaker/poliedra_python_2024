class Conto():
    def __init__(self, saldo=0):
        self.__saldo = saldo
    
    def view_saldo(self):
        print(f"saldo: {self.__saldo}")
    
    def deposito(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"versati {importo}$")
        else:
            print("importo non valido (<= 0!)")
    def prelevo(self, importo):
        if importo > self.__saldo:
            print("saldo insuff!!")
        elif importo > 0:            
            self.__saldo -= importo
        else:
            print("importo non valido")
    
saldo_iniziale = 100

cc = Conto(saldo_iniziale)
cc.view_saldo()
cc.deposito(50)
cc.view_saldo()
cc.prelevo(25)
cc.view_saldo()
cc.prelevo(200)
cc.view_saldo()