import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("300x200")

fr1 = tk.Frame(app, height=50)
fr1['background'] = '#fdffc7'
fr1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

fr2 = tk.Frame(app, height=50)
fr2['background'] = '#c7f9ff'
fr2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

fr3 = tk.Frame(fr2, width=40, height=50)
fr3['background'] = 'white'
fr3.pack(fill=tk.BOTH, side=tk.LEFT)

tk.Button(fr1, text="bt1").pack()
tk.Button(fr2, text="bt2").pack()
tk.Button(fr3, text="bt3").pack()

app.mainloop()





