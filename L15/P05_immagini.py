import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("700x500")

img = "./cat-720x719.png"
pic = tk.PhotoImage(file=img)

l1 = tk.Label(app)
l1['image'] = pic
l1['text'] = "un gatto"
l1['compound'] = 'top'
l1.pack()

app.mainloop()



