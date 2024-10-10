import csv

class Registro():
    
    def __init__(self):
        self.studenti = []
    
    def add(self, nome, voto):
        self.studenti.append( { 'nome':nome, 'voto':voto } )
        
    def save(self, nomefile):
        with open(nomefile, mode='w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=['nome', 'voto'] )
            w.writeheader()
            w.writerows(self.studenti)
        print("dati salvati")
    
    def load(self, nomefile):
        self.studenti = []
        with open(nomefile, mode='r') as f:
            r = csv.DictReader(f)
            for el in r:
                self.studenti.append(el)
        print("dati caricati")
            
    
    def show(self):
        for p in self.studenti:
            nome = p['nome']
            voto = p['voto']
            print(f"{nome}: {voto}")
    

if __name__ == '__main__':
    r = Registro()
    
    r.add("Mario", 18)
    r.add("Luigi", 24)
    r.save("persone.csv")
    r.show()
    
    r.load("persone.csv")
    r.show()