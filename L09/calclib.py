
class Calc():
    
    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.operazione = "?"
        self.result = 0
        
    def setOperando1(self, n):
        self.op1 = int(n)
        
    def setOperando2(self, n):
        self.op2 = int(n)
        
    def setOperazione(self, op):
        self.operazione = op
        
    def getResult(self):
        self.calcola()
        return self.result
    
    def calcola(self):
        if self.operazione == '+':
            self.result = self.op1 + self.op2
        elif self.operazione == '-':
            self.result = self.op1 - self.op2
        else:
            self.result = 0
            
    def __str__(self):
        return f"{self.op1} {self.operazione} {self.op2} = {self.result}"

if __name__ == "__main__":
    print("non è eseguibile")