import random

class LetturaFuoriScala(Exception):
    def __init__(self, valore, message="Valore fuori scala"):
        self.valore = valore
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"err"

while True:
    val = random.randint(0, 100)
    print(f"lettura sensore: {val}")
    if (val > 80) or (val < 20):
        raise LetturaFuoriScala(val)
        