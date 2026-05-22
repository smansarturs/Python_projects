import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Currency Converter")
window.geometry("420x300")
window.resizable(False, False)

# ------------------- DATA -------------------
rates = {
    "EUR": 1.0,
    "USD": 1.17,
    "GBP": 0.87,
    "PLN": 4.25,
    "RUB": 90.30
}

currencies = list(rates.keys())

# ------------------- VARIABLES -------------------
amount_var = tk.StringVar()
from_currency = tk.StringVar(value="EUR")
to_currency = tk.StringVar(value="USD")
result_var = tk.StringVar(value="Enter amount and select currencies")

# ------------------- STYLE -------------------
style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Segoe UI", 10))
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))

# ------------------- FUNCTIONS -------------------
def convert():
    try:
        amount = float(amount_var.get())
        from_cur = from_currency.get()
        to_cur = to_currency.get()

        euros = amount / rates[from_cur]
        converted = euros * rates[to_cur]

        result_var.set(f"{amount} {from_cur} = {converted:.2f} {to_cur}")

    except:
        result_var.set("Invalid input")

# ------------------- UI -------------------
main = ttk.Frame(window, padding=20)
main.pack(fill="both", expand=True)

ttk.Label(main, text="Currency Converter", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(main, text="Amount").grid(row=1, column=0, sticky="w")
ttk.Entry(main, textvariable=amount_var).grid(row=1, column=1)

ttk.Label(main, text="From").grid(row=2, column=0, sticky="w")
ttk.Combobox(main, textvariable=from_currency, values=currencies, state="readonly").grid(row=2, column=1)

ttk.Label(main, text="To").grid(row=3, column=0, sticky="w")
ttk.Combobox(main, textvariable=to_currency, values=currencies, state="readonly").grid(row=3, column=1)

ttk.Button(main, text="Convert", command=convert).grid(row=4, column=0, columnspan=2, pady=15)

ttk.Label(main, textvariable=result_var, font=("Segoe UI", 12)).grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()