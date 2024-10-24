import tkinter as tk

app = tk.Tk()
app.title("App 01")
app.geometry("300x200")

fr1 = tk.Frame(app)
fr1['background'] = '#fdffc7'
fr1.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

fr2 = tk.Frame(app)
fr2['background'] = '#c7f9ff'
fr2.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

tk.Button(fr1, text="BT1").pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(fr1, text="BT2").pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(fr1, text="BT3").pack(side=tk.LEFT, padx=5, pady=5)

tk.Button(fr2, text="BT4").pack(side=tk.LEFT, padx=5, pady=5)

app.mainloop()




