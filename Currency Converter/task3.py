import requests
import tkinter as tk
from tkinter import ttk

#GUI setup
api_key = 'YOUR_API_KEY'  # Replace with your Open Exchange Rates API key
root = tk.Tk()
root.title("Currency Converter")
root.config(background='#06e3dd')
root.geometry('600x800')

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {
        'apikey': api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)

        if rate:
            return rate
        else:
            print(f"Error: Could not find exchange rate for {target_currency}")
    else:
        print(f"Error: Unable to fetch exchange rates. Status code: {response.status_code}")

    return None

def convert_currency(api_key, amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def calculate_conversion():
    amount = float(amount_entry.get())
    base_currency = base_currency_entry.get().upper()
    target_currency = target_currency_entry.get().upper()

    converted_amount = convert_currency(api_key, amount, base_currency, target_currency)

    if converted_amount is not None:
        result_label.config(text=f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        result_label.config(text="Conversion failed.")

#
#label
tk.Label(root,text='Currency Converter',font=('Helvetica',40,'bold'),background='#06e3dd').place(x=500,y=150)

# Create and pack widgets
amount_label = ttk.Label(root, text="Amount",font=('Helvetica',15,'bold'),background='#06e3dd')
amount_label.place(x=400,y=300)

amount_entry = ttk.Entry(root,width=20,font=('Helvetica',10,'bold'))
amount_entry.place(x=400,y=335)

base_currency_label = ttk.Label(root, text="Base Currency",font=('Helvetica',15,'bold'),background='#06e3dd')
base_currency_label.place(x=700,y=300)

base_currency_entry = ttk.Entry(root,width=25,font=('Helvetica',10,'bold'))
base_currency_entry.place(x=700,y=335)

target_currency_label = ttk.Label(root, text="Target Currency",font=('Helvetica',15,'bold'),background='#06e3dd')
target_currency_label.place(x=1000,y=300)

target_currency_entry = ttk.Entry(root,width=25,font=('Helvetica',10,'bold'))
target_currency_entry.place(x=1000,y=335)

convert_button = ttk.Button(root, text="Exchange", command=calculate_conversion,width=10)
convert_button.place(x=700,y=400)

result_label = ttk.Label(root, text="",background='#06e3dd',font=('Helvetica',15,'bold'))
result_label.place(x=650,y=450)

root.mainloop()
