import tkinter as tk

def clic():
    s = msg.get()
    print(s)
    msg.delete(0, tk.END)
    msg.insert(0, "ciao")

app = tk.Tk()
app.title("App 01")
app.geometry("300x200")

bt = tk.Button(text="Saluta!", command=clic)
bt.pack()

msg = tk.Entry(width=50)
msg.pack()

app.mainloop()
