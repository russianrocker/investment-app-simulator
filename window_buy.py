#модуль window_buy
#Запуск окон покупки ценных бумаг/товаров

from tkinter import *
from tkinter import messagebox
import shelve

import main_window

def usd():
    variables = shelve.open('variables.dat')
    
    usd_buy=Toplevel()
    usd_buy.title('USD: Обмен валют')
    usd_buy.geometry('300x25')

    summ_of_buy_label = Label(usd_buy, text='Сумма покупки, USD')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(usd_buy, from_=0, to=round(variables['balance'][0]/variables['usd_buy'][7], 2), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', float(summ_of_buy_spinbox.get()), 'USD за', round(float(summ_of_buy_spinbox.get())*variables['usd_buy'][7], 2), 'RUB?'))

        if confirmation == True:
            usd_bought = variables['usd_bought'][0] + float(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['usd_buy'][7]
            variables['balance'] = [balance_change]
            variables['usd_bought'] = [usd_bought]
            variables.sync()
            usd_buy.destroy()

    button_buy = Button(usd_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        usd_buy.destroy()
    
    button_back = Button(usd_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def eur():
    variables = shelve.open('variables.dat')
    
    eur_buy=Toplevel()
    eur_buy.title('EUR: Обмен валют')
    eur_buy.geometry('300x25')

    summ_of_buy_label = Label(eur_buy, text='Сумма покупки, EUR')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(eur_buy, from_=0, to=round(variables['balance'][0]/variables['eur_buy'][7], 2), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', float(summ_of_buy_spinbox.get()), 'EUR за', round(float(summ_of_buy_spinbox.get())*variables['eur_buy'][7], 2), 'RUB?'))

        if confirmation == True:
            eur_bought = variables['eur_bought'][0] + float(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['eur_buy'][7]
            variables['balance'] = [balance_change]
            variables['eur_bought'] = [eur_bought]
            variables.sync()
            eur_buy.destroy()

    button_buy = Button(eur_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        eur_buy.destroy()
    
    button_back = Button(eur_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def chf():
    variables = shelve.open('variables.dat')
    
    chf_buy=Toplevel()
    chf_buy.title('CHF: Обмен валют')
    chf_buy.geometry('300x25')

    summ_of_buy_label = Label(chf_buy, text='Сумма покупки, CHF')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(chf_buy, from_=0, to=round(variables['balance'][0]/variables['chf_buy'][7], 2), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', float(summ_of_buy_spinbox.get()), 'CHF за', round(float(summ_of_buy_spinbox.get())*variables['chf_buy'][7], 2), 'RUB?'))

        if confirmation == True:
            chf_bought = variables['chf_bought'][0] + float(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['chf_buy'][7]
            variables['balance'] = [balance_change]
            variables['chf_bought'] = [chf_bought]
            variables.sync()
            chf_buy.destroy()

    button_buy = Button(chf_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        chf_buy.destroy()
    
    button_back = Button(chf_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def gbp():
    variables = shelve.open('variables.dat')
    
    gbp_buy=Toplevel()
    gbp_buy.title('GBP: Обмен валют')
    gbp_buy.geometry('300x25')

    summ_of_buy_label = Label(gbp_buy, text='Сумма покупки, GBP')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(gbp_buy, from_=0, to=round(variables['balance'][0]/variables['gbp_buy'][7], 2), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', float(summ_of_buy_spinbox.get()), 'GBP за', round(float(summ_of_buy_spinbox.get())*variables['gbp_buy'][7], 2), 'RUB?'))

        if confirmation == True:
            gbp_bought = variables['gbp_bought'][0] + float(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['gbp_buy'][7]
            variables['balance'] = [balance_change]
            variables['gbp_bought'] = [gbp_bought]
            variables.sync()
            gbp_buy.destroy()

    button_buy = Button(gbp_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        gbp_buy.destroy()
    
    button_back = Button(gbp_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def jpy():
    variables = shelve.open('variables.dat')
    
    jpy_buy=Toplevel()
    jpy_buy.title('JPY: Обмен валют')
    jpy_buy.geometry('300x25')

    summ_of_buy_label = Label(jpy_buy, text='Сумма покупки, JPY')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(jpy_buy, from_=0, to=round(variables['balance'][0]/variables['jpy_buy'][7], 2), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', float(summ_of_buy_spinbox.get()), 'JPY за', round(float(summ_of_buy_spinbox.get())*variables['jpy_buy'][7], 2), 'RUB?'))

        if confirmation == True:
            jpy_bought = variables['jpy_bought'][0] + float(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['jpy_buy'][7]
            variables['balance'] = [balance_change]
            variables['jpy_bought'] = [jpy_bought]
            variables.sync()
            jpy_buy.destroy()

    button_buy = Button(jpy_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        jpy_buy.destroy()
    
    button_back = Button(jpy_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

#=====================================================================
def gazprom():
    variables = shelve.open('variables.dat')
    
    gazprom_buy=Toplevel()
    gazprom_buy.title('Gazprom: Покупка акций')
    gazprom_buy.geometry('300x25')

    summ_of_buy_label = Label(gazprom_buy, text='Количество')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(gazprom_buy, from_=0, to=round(variables['balance'][0]/variables['gazprom'][7]), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', summ_of_buy_spinbox.get(), 'шт. акции Gazprom за', round(float(summ_of_buy_spinbox.get())*variables['gazprom'][7], 2), 'RUB?'))

        if confirmation == True:
            gazprom_bought = variables['gazprom_bought_pcs'][0] + int(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['gazprom'][7]
            variables['balance'] = [balance_change]
            variables['gazprom_bought_pcs'] = [gazprom_bought]
            variables.sync()
            gazprom_buy.destroy()

    button_buy = Button(gazprom_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        gazprom_buy.destroy()
    
    button_back = Button(gazprom_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def avtovaz():
    variables = shelve.open('variables.dat')
    
    avtovaz_buy=Toplevel()
    avtovaz_buy.title('Avtovaz: Покупка акций')
    avtovaz_buy.geometry('300x25')

    summ_of_buy_label = Label(avtovaz_buy, text='Количество')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(avtovaz_buy, from_=0, to=round(variables['balance'][0]/variables['avtovaz'][7]), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', summ_of_buy_spinbox.get(), 'шт. акции Avtovaz за', round(float(summ_of_buy_spinbox.get())*variables['avtovaz'][7], 2), 'RUB?'))

        if confirmation == True:
            avtovaz_bought = variables['avtovaz_bought_pcs'][0] + int(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['avtovaz'][7]
            variables['balance'] = [balance_change]
            variables['avtovaz_bought_pcs'] = [avtovaz_bought]
            variables.sync()
            avtovaz_buy.destroy()

    button_buy = Button(avtovaz_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        avtovaz_buy.destroy()
    
    button_back = Button(avtovaz_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def aeroflot():
    variables = shelve.open('variables.dat')
    
    aeroflot_buy=Toplevel()
    aeroflot_buy.title('Gazprom: Покупка акций')
    aeroflot_buy.geometry('300x25')

    summ_of_buy_label = Label(aeroflot_buy, text='Количество')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(aeroflot_buy, from_=0, to=round(variables['balance'][0]/variables['aeroflot'][7]), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', summ_of_buy_spinbox.get(), 'шт. акции Aeroflot за', round(float(summ_of_buy_spinbox.get())*variables['aeroflot'][7], 2), 'RUB?'))

        if confirmation == True:
            aeroflot_bought = variables['aeroflot_bought_pcs'][0] + int(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['aeroflot'][7]
            variables['balance'] = [balance_change]
            variables['aeroflot_bought_pcs'] = [aeroflot_bought]
            variables.sync()
            aeroflot_buy.destroy()

    button_buy = Button(aeroflot_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        aeroflot_buy.destroy()
    
    button_back = Button(aeroflot_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def nornickel():
    variables = shelve.open('variables.dat')
    
    nornickel_buy=Toplevel()
    nornickel_buy.title('Nornickel: Покупка акций')
    nornickel_buy.geometry('300x25')

    summ_of_buy_label = Label(nornickel_buy, text='Количество')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(nornickel_buy, from_=0, to=round(variables['balance'][0]/variables['nornickel'][7]), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', summ_of_buy_spinbox.get(), 'шт. акции Nornickel за', round(float(summ_of_buy_spinbox.get())*variables['nornickel'][7], 2), 'RUB?'))

        if confirmation == True:
            nornickel_bought = variables['nornickel_bought_pcs'][0] + int(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['nornickel'][7]
            variables['balance'] = [balance_change]
            variables['nornickel_bought_pcs'] = [nornickel_bought]
            variables.sync()
            nornickel_buy.destroy()

    button_buy = Button(nornickel_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        nornickel_buy.destroy()
    
    button_back = Button(nornickel_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

def lukoil():
    variables = shelve.open('variables.dat')
    
    lukoil_buy=Toplevel()
    lukoil_buy.title('lukoil: Покупка акций')
    lukoil_buy.geometry('300x25')

    summ_of_buy_label = Label(lukoil_buy, text='Количество')
    summ_of_buy_label.grid(column=0, row=0)

    summ_of_buy_spinbox = Spinbox(lukoil_buy, from_=0, to=round(variables['balance'][0]/variables['lukoil'][7]), width=7)
    summ_of_buy_spinbox.grid(column=1, row=0)

    def buy_confirmation():
        confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Купить', summ_of_buy_spinbox.get(), 'шт. акции Lukoil за', round(float(summ_of_buy_spinbox.get())*variables['lukoil'][7], 2), 'RUB?'))

        if confirmation == True:
            lukoil_bought = variables['lukoil_bought_pcs'][0] + int(summ_of_buy_spinbox.get())
            balance_change = variables['balance'][0] - float(summ_of_buy_spinbox.get())*variables['lukoil'][7]
            variables['balance'] = [balance_change]
            variables['lukoil_bought_pcs'] = [lukoil_bought]
            variables.sync()
            lukoil_buy.destroy()

    button_buy = Button(lukoil_buy, text='Купить', command=buy_confirmation)
    button_buy.grid(column=2, row=0)

    def close_window():
        lukoil_buy.destroy()
    
    button_back = Button(lukoil_buy, text='Отмена', command=close_window)
    button_back.grid(column=3, row=0)

#=======================================================================================

    
