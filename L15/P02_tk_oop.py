import tkinter as tk
from tkinter.messagebox import showinfo

class myApp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("OOP App")
        self.geometry("500x400")
        
        self.l1 = tk.Label(text="Come ti chiami?")
        self.l1.pack()
        
        self.nome = tk.Entry()
        self.nome.pack()
        
        self.bt = tk.Button(self, text="Click me!")
        self.bt['command'] = self.bt_clicked
        self.bt.pack()
        
        self.l2 = tk.Label(text="")
        self.l2.pack()
        
        self.bt2 = tk.Button(self, text="popup!")
        self.bt2['command'] = self.bt2_clicked
        self.bt2.pack()

    def bt_clicked(self):
        n = self.nome.get()
        print(n)
        self.l2['text'] = "Ciao, " + n
    
    def bt2_clicked(self):
        showinfo(title="Info...", message="Pop Up Message!")
        

if __name__ == '__main__':
    app = myApp()
    app.mainloop()