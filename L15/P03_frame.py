import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("700x500")

#fr = tk.Frame(master=app)
fr = tk.Frame(app)
fr['width'] = 200
fr['height'] = 100
fr['borderwidth'] = 2
fr['relief'] = 'ridge'
fr['background'] = '#1fb5d0'
fr.pack()

app.mainloop()

