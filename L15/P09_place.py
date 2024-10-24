import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("300x200")

l1 = tk.Label(app, text="Nome: ")
l1.place(x=10, y=10)
tk.Entry(app).place(x=80, y=10)

tk.Label(app, text="pass: ").place(x=10, y=40)
tk.Entry(app).place(x=80, y=40)

tk.Button(text='login').place(x=205, y=70)

app.mainloop()






