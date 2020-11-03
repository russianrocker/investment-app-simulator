#модуль window_sale
#Запуск окон продажи ценных бумаг/товаров

from tkinter import *
from tkinter import messagebox
import shelve

def usd():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('USD: Обмен валют', 'Нет USD для продажи')

    else:
        usd_sale=Toplevel()
        usd_sale.title('USD: Обмен валют')
        usd_sale.geometry('300x25')

        summ_of_sale_label = Label(usd_sale, text='Сумма продажи, USD')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(usd_sale, from_=0, to=round(variables['usd_bought'][0], 2), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', float(summ_of_sale_spinbox.get()), 'USD за', round(float(summ_of_sale_spinbox.get())*variables['usd_sale'][7], 2), 'RUB?'))

            if confirmation == True:
                usd_bought = variables['usd_bought'][0] - float(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['usd_sale'][7]
                variables['balance'] = [balance_change]
                variables['usd_bought'] = [usd_bought]
                variables.sync()
                usd_sale.destroy()

        button_sale = Button(usd_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            usd_sale.destroy()
    
        button_back = Button(usd_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def eur():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('EUR: Обмен валют', 'Нет EUR для продажи')

    else:    
        eur_sale=Toplevel()
        eur_sale.title('EUR: Обмен валют')
        eur_sale.geometry('300x25')

        summ_of_sale_label = Label(eur_sale, text='Сумма продажи, EUR')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(eur_sale, from_=0, to=round(variables['eur_bought'][0], 2), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', float(summ_of_sale_spinbox.get()), 'EUR за', round(float(summ_of_sale_spinbox.get())*variables['eur_sale'][7], 2), 'RUB?'))

            if confirmation == True:
                eur_bought = variables['eur_bought'][0] - float(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['eur_sale'][7]
                variables['balance'] = [balance_change]
                variables['eur_bought'] = [eur_bought]
                variables.sync()
                eur_sale.destroy()

        button_sale = Button(eur_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            eur_sale.destroy()
    
        button_back = Button(eur_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def chf():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('CHF: Обмен валют', 'Нет CHF для продажи')

    else:
        chf_sale=Toplevel()
        chf_sale.title('CHF: Обмен валют')
        chf_sale.geometry('300x25')

        summ_of_sale_label = Label(chf_sale, text='Сумма продажи, CHF')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(chf_sale, from_=0, to=round(variables['chf_bought'][0], 2), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', float(summ_of_sale_spinbox.get()), 'CHF за', round(float(summ_of_sale_spinbox.get())*variables['chf_sale'][7], 2), 'RUB?'))

            if confirmation == True:
                chf_bought = variables['chf_bought'][0] - float(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['chf_sale'][7]
                variables['balance'] = [balance_change]
                variables['chf_bought'] = [chf_bought]
                variables.sync()
                chf_sale.destroy()

        button_sale = Button(chf_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            chf_sale.destroy()
    
        button_back = Button(chf_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def gbp():
    variables = shelve.open('variables.dat')

    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('GBP: Обмен валют', 'Нет GBP для продажи')

    else:
        gbp_sale=Toplevel()
        gbp_sale.title('GBP: Обмен валют')
        gbp_sale.geometry('300x25')

        summ_of_sale_label = Label(gbp_sale, text='Сумма продажи, GBP')
        summ_of_sale_label.grid(column=0, row=0)
    
        summ_of_sale_spinbox = Spinbox(gbp_sale, from_=0, to=round(variables['gbp_bought'][0], 2), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', float(summ_of_sale_spinbox.get()), 'GBP за', round(float(summ_of_sale_spinbox.get())*variables['gbp_sale'][7], 2), 'RUB?'))

            if confirmation == True:
                gbp_bought = variables['gbp_bought'][0] - float(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['gbp_sale'][7]
                variables['balance'] = [balance_change]
                variables['gbp_bought'] = [gbp_bought]
                variables.sync()
                gbp_sale.destroy()

        button_sale = Button(gbp_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            gbp_sale.destroy()
    
        button_back = Button(gbp_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def jpy():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('JPY: Обмен валют', 'Нет JPY для продажи')

    else:
        jpy_sale=Toplevel()
        jpy_sale.title('JPY: Обмен валют')
        jpy_sale.geometry('300x25')

        summ_of_sale_label = Label(jpy_sale, text='Сумма продажи, JPY')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(jpy_sale, from_=0, to=round(variables['jpy_bought'][0], 2), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', float(summ_of_sale_spinbox.get()), 'JPY за', round(float(summ_of_sale_spinbox.get())*variables['jpy_sale'][7], 2), 'RUB?'))

            if confirmation == True:
                jpy_bought = variables['jpy_bought'][0] - float(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['jpy_sale'][7]
                variables['balance'] = [balance_change]
                variables['jpy_bought'] = [jpy_bought]
                variables.sync()
                jpy_sale.destroy()

        button_sale = Button(jpy_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            jpy_sale.destroy()
    
        button_back = Button(jpy_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

#=====================================================================
def gazprom():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('Gazprom: Продажа акций', 'Нет акций для продажи')

    else:
        gazprom_sale=Toplevel()
        gazprom_sale.title('Gazprom: Продажа акций')
        gazprom_sale.geometry('300x25')
    
        summ_of_sale_label = Label(gazprom_sale, text='Количество')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(gazprom_sale, from_=0, to=round(variables['gazprom_bought_pcs'][0]), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', summ_of_sale_spinbox.get(), 'шт. акций Gazprom за', round(float(summ_of_sale_spinbox.get())*variables['gazprom'][7], 2), 'RUB?'))

            if confirmation == True:
                gazprom_bought = variables['gazprom_bought_pcs'][0] - int(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['gazprom'][7]
                variables['balance'] = [balance_change]
                variables['gazprom_bought_pcs'] = [gazprom_bought]
                variables.sync()
                gazprom_sale.destroy()

        button_sale = Button(gazprom_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            gazprom_buy.destroy()
    
        button_back = Button(gazprom_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def avtovaz():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('Avtovaz: Продажа акций', 'Нет акций для продажи')

    else:
        avtovaz_sale=Toplevel()
        avtovaz_sale.title('Avtovaz: Продажа акций')
        avtovaz_sale.geometry('300x25')

        summ_of_sale_label = Label(avtovaz_sale, text='Количество')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(avtovaz_sale, from_=0, to=round(variables['avtovaz_bought_pcs'][0]), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', summ_of_sale_spinbox.get(), 'шт. акций Avtovaz за', round(float(summ_of_sale_spinbox.get())*variables['avtovaz'][7], 2), 'RUB?'))

            if confirmation == True:
                avtovaz_bought = variables['avtovaz_bought_pcs'][0] - int(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['avtovaz'][7]
                variables['balance'] = [balance_change]
                variables['avtovaz_bought_pcs'] = [avtovaz_bought]
                variables.sync()
                avtovaz_sale.destroy()

        button_sale = Button(avtovaz_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            avtovaz_sale.destroy()
    
        button_back = Button(avtovaz_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def aeroflot():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('Aeroflot: Продажа акций', 'Нет акций для продажи')

    else:
        aeroflot_sale=Toplevel()
        aeroflot_sale.title('Aeroflot: Продажа акций')
        aeroflot_sale.geometry('300x25')

        summ_of_sale_label = Label(aeroflot_sale, text='Количество')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(aeroflot_sale, from_=0, to=round(variables['aeroflot_bought_pcs'][0]), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', summ_of_sale_spinbox.get(), 'шт. акций Aeroflot за', round(float(summ_of_sale_spinbox.get())*variables['aeroflot'][7], 2), 'RUB?'))

            if confirmation == True:
                aeroflot_bought = variables['aeroflot_bought_pcs'][0] - int(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['aeroflot'][7]
                variables['balance'] = [balance_change]
                variables['aeroflot_bought_pcs'] = [aeroflot_bought]
                variables.sync()
                aeroflot_sale.destroy()

        button_sale = Button(aeroflot_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            aeroflot_sale.destroy()
        
        button_back = Button(aeroflot_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def nornickel():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('Nornickel: Продажа акций', 'Нет акций для продажи')

    else:
        nornickel_sale=Toplevel()
        nornickel_sale.title('Nornickel: Продажа акций')
        nornickel_sale.geometry('300x25')

        summ_of_sale_label = Label(nornickel_sale, text='Количество')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(nornickel_sale, from_=0, to=round(variables['nornickel_bought_pcs'][0]), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', summ_of_sale_spinbox.get(), 'шт. акций Nornickel за', round(float(summ_of_sale_spinbox.get())*variables['nornickel'][7], 2), 'RUB?'))

            if confirmation == True:
                nornickel_bought = variables['nornickel_bought_pcs'][0] - int(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['nornickel'][7]
                variables['balance'] = [balance_change]
                variables['nornickel_bought_pcs'] = [nornickel_bought]
                variables.sync()
                nornickel_sale.destroy()

        button_sale = Button(nornickel_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            nornickel_sale.destroy()
        
        button_back = Button(nornickel_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)

def lukoil():
    variables = shelve.open('variables.dat')
    if variables['usd_bought'][0] <= 0:
        messagebox.showerror('Lukoil: Продажа акций', 'Нет акций для продажи')

    else:
        lukoil_sale=Toplevel()
        lukoil_sale.title('lukoil: Продажа акций')
        lukoil_sale.geometry('300x25')

        summ_of_sale_label = Label(lukoil_sale, text='Количество')
        summ_of_sale_label.grid(column=0, row=0)

        summ_of_sale_spinbox = Spinbox(lukoil_sale, from_=0, to=round(variables['lukoil_bought_pcs'][0]), width=7)
        summ_of_sale_spinbox.grid(column=1, row=0)

        def buy_confirmation():
            confirmation = messagebox.askyesno('Предупреждение', '{} {} {} {} {}'.format('Продать', summ_of_sale_spinbox.get(), 'шт. акций Lukoil за', round(float(summ_of_sale_spinbox.get())*variables['lukoil'][7], 2), 'RUB?'))

            if confirmation == True:
                lukoil_bought = variables['lukoil_bought_pcs'][0] - int(summ_of_sale_spinbox.get())
                balance_change = variables['balance'][0] + float(summ_of_sale_spinbox.get())*variables['lukoil'][7]
                variables['balance'] = [balance_change]
                variables['lukoil_bought_pcs'] = [lukoil_bought]
                variables.sync()
                lukoil_sale.destroy()

        button_sale = Button(lukoil_sale, text='Продать', command=buy_confirmation)
        button_sale.grid(column=2, row=0)

        def close_window():
            lukoil_sale.destroy()
        
        button_back = Button(lukoil_sale, text='Отмена', command=close_window)
        button_back.grid(column=3, row=0)
