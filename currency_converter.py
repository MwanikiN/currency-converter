""" a currency converter UI app using python. This app should prompt the user to
choose a base currency to work with i.e USD or Yen etc. It should also receive user input
of the amount to convert
 """
from urllib.request import urlopen
from tkinter import *
from tkinter import ttk
import json
import tkinter as tk


class CurrencyConverter():
  def __init__(self,url):
    self.url = url
    try:
        response = urlopen(url)
        data_json = json.loads(response.read())
        data_dict = dict(data_json)
        self.data =data_dict['rates']
    except:
        raise ConnectionError ("Response cannot be retrieved")
  

  def calc_rates(self, former_currency, new_currency, amount):
    self.former_currency = former_currency
    self.new_currency = new_currency
    self.amount = amount
    if new_currency == 'USD':
      if former_currency != 'USD':
        amount = amount/self.data[former_currency]
    else:
      initial_amount = amount/self.data[former_currency]
      amount = initial_amount*self.data[new_currency]
    return amount

converted_rates = CurrencyConverter("https://api.exchangerate-api.com/v4/latest/USD")


class DisplayConverter(tk.Tk):
    def __init__(self, converted_rates):
        tk.Tk.__init__(self)
        self.title('Currency_Converter')
        self.currency_converter = converted_rates
        self.geometry("500x500")
        self.config(bg='dark blue')

        self.header = Label(self, text = 'Currency Convertor on the go',  fg = 'white', bg='dark blue', relief = tk.RAISED, borderwidth = 5, justify=tk.CENTER)
        self.header.config(font = ('Times New Roman',14,'bold'))
        self.header.place(x = 120 , y = 50)
        
        self.amount = Entry(self, bd = 5, relief = tk.RIDGE, justify = tk.CENTER,validate='key')
        self.converted_amount = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 5)
        self.amount.place(x = 35, y = 225)
        self.converted_amount.place(x = 305, y = 225)
        
        self.former_currency = StringVar(self)
        self.former_currency.set("KES") 
        self.new_currency = StringVar(self)
        self.new_currency.set("USD")

        self.former_currency_menu = OptionMenu(self, self.former_currency, *list(self.currency_converter.data.keys()))
        self.new_currency_menu = OptionMenu(self, self.new_currency, *list(self.currency_converter.data.keys()))
        self.former_currency_menu.place(x = 50, y= 150)
        self.new_currency_menu.place(x = 325, y= 150)
        
        self.convert = Button(self, text = "Convert", fg = "white", bg= 'dark blue', command = self.perform) 
        self.convert.config(font=('Times New Roman', 10, 'bold'))
        self.convert.place(x = 225, y = 300)

    def perform(self,):
        amount = float(self.amount.get())
        initial_currency = self.former_currency.get()
        changed_currency = self.new_currency.get()
        convert_amount= self.currency_converter.calc_rates(initial_currency,changed_currency,amount)
        convert_amount = round(convert_amount, 4)
     
        self.converted_amount.config(text = str(convert_amount))

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
 
    DisplayConverter(converter)
    mainloop()
   