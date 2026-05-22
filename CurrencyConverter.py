import tkinter as tk

window = tk.Tk()
window.title("Currency converter")
window.geometry("400x330")
window.resizable(False, False)

from_currency = tk.StringVar()
to_currency = tk.StringVar()
result = tk.StringVar()


entry_amount = tk.Entry(window)

rates = {
    "EUR" : 1.0,
    "USD" : 1.17,
    "GBP" : 0.87,
    "PLN" : 4.25,
    "RUB" : 90.30
}

def convert():
    try:
        amount = float(entry_amount.get())
        from_cur = from_currency.get().upper()
        to_cur = to_currency.get().upper()

        euros = amount / rates[from_cur]
        converted = euros * rates[to_cur]

        result.set(f"{amount} {from_cur} = {round(converted, 2)} {to_cur}")
    except:
        result.set("Input error")

tk.Label(window, text="Sum").grid(row = 0, column = 0, padx = 10, pady = 10)
entry_amount = tk.Entry(window)
entry_amount.grid(row=0, column=1)

tk.Label(window, text="From currency").grid(row=1, column=0)
tk.Entry(window, textvariable=from_currency).grid(row=1, column=1)

tk.Label(window, text="To currency").grid(row=2, column=0)
tk.Entry(window, textvariable=to_currency).grid(row=2, column=1)

tk.Button(window, text="Convert", command=convert).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(window, textvariable=result, font=("Arial", 14)).grid(row=4, column=0, columnspan=2)

window.mainloop()
