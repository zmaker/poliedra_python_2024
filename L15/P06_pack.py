import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("700x500")

l1 = tk.Button(app, text="b1")
l1['background'] = "#cc0000"
l1.pack(fill=tk.X, padx=10, pady=10, side=tk.TOP)

l2 = tk.Button(app, text="b2").pack()

l3 = tk.Button(app, text="b3").pack()


app.mainloop()



