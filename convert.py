import tkinter as tk

window = tk.Tk()
window.title("Конвертер")

# 1. переменные
from_currency = tk.StringVar()
to_currency = tk.StringVar()
result = tk.StringVar()

# 2. элементы
tk.Label(window, text="Сумма").pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

tk.Label(window, text="Из валюты").pack()
tk.Entry(window, textvariable=from_currency).pack()

tk.Label(window, text="В валюту").pack()
tk.Entry(window, textvariable=to_currency).pack()

tk.Button(window, text="Конвертировать").pack()

tk.Label(window, textvariable=result).pack()

# 3. запуск
window.mainloop()