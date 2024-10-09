#esercizio ereditarietà

class Persona():
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def presenta(self):
        print(f"Ciao mi chiamo {self.nome}, {self.cognome} ed ho {self.eta} anni.")
    
class Studente(Persona):
    def __init__(self, nome, cognome, eta, scuola):
        super().__init__(nome, cognome, eta)
        self.scuola = scuola
    
    def dettaglioStudente(self):
        self.presenta()
        print("La mia scuola è: ", self. scuola)
        
s1 = Studente("Mario", "Rossi", 23, "polimi")
s1.presenta()
s1.dettaglioStudente()