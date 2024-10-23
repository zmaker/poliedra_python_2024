import tkinter as tk

def btClicked():
    print("clic")

def btPressed(event):
    print("bt2")
    print(event)

app = tk.Tk()
app.title("My App")
app.geometry("300x200")

lb = tk.Label(text="Hello!")
lb.pack()

bt1 = tk.Button(text="click me", command=btClicked)
bt1.pack()

bt2 = tk.Button(text="click me too")
bt2.pack()
bt2.bind('<Button-1>', btPressed)


app.mainloop()
print("end")
