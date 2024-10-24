import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("700x500")

l1 = tk.Label(app)
l1['text'] = "hello world!"
l1['font'] = ("Bangers", 40)
l1.pack()

l2 = tk.Label(app)
l2['text'] = "Font di tipo Ubuntu"
l2['font'] = ("Ubuntu", 40)
l2.pack()

app.mainloop()


