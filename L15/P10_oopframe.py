import tkinter as tk
from tkinter.messagebox import showinfo

class myApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('FrameApp')
        self.geometry("300x200")

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self['background'] = "#ccccff"
        
        self.label = tk.Label(self, text="Hello")
        self.label.pack()
        
        self.pack(fill=tk.BOTH, expand=True)

if __name__ == '__main__':
    app = myApp()
    fr = MainFrame(app)
    app.mainloop()
