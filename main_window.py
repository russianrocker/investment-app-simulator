#==========================================
#Модуль window_main
#Главное окно программы
#==========================================
#Модули
#------------------------------------------
#Модули для создания GUI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#------------------------------------------
#Модуль для генерации псевдослучайных чисел
import random
#------------------------------------------
#Модуль для создания файла сохранения
import shelve
#------------------------------------------
#Прочие модули
import reset             
import window_details    
import window_buy
import window_sale
import next_day
import about
#------------------------------------------
#Переменные
variables = shelve.open('variables.dat')
spread = random.random()
#==========================================
#Основная часть
def init():    
    def update():
        window_main.title('{} {} {} {} {} {}'.format('День', variables['day'][0], '|', 'Баланс:', round(variables['balance'][0], 2), 'RUB'))
        
        usd_buy_label.configure(text=round(variables['usd_buy'][7], 2))
        usd_sale_label.configure(text=round(variables['usd_sale'][7], 2))
        usd_bought_label.configure(text=round(variables['usd_bought'][0], 2))

        eur_buy_label.configure(text=round(variables['eur_buy'][7], 2))
        eur_sale_label.configure(text=round(variables['eur_sale'][7], 2))
        eur_bought_label.configure(text=round(variables['eur_bought'][0], 2))

        chf_buy_label.configure(text=round(variables['chf_buy'][7], 2))
        chf_sale_label.configure(text=round(variables['chf_sale'][7], 2))
        chf_bought_label.configure(text=round(variables['chf_bought'][0], 2))

        gbp_buy_label.configure(text=round(variables['gbp_buy'][7], 2))
        gbp_sale_label.configure(text=round(variables['gbp_sale'][7], 2))
        gbp_bought_label.configure(text=round(variables['gbp_bought'][0], 2))

        jpy_buy_label.configure(text=round(variables['jpy_buy'][7], 2))
        jpy_sale_label.configure(text=round(variables['jpy_sale'][7], 2))
        jpy_bought_label.configure(text=round(variables['jpy_bought'][0], 2))

        gazprom_price_label.configure(text=round(variables['gazprom'][7], 2))
        gazprom_bought_pcs_label.configure(text=variables['gazprom_bought_pcs'][0])

        avtovaz_price_label.configure(text=round(variables['avtovaz'][7], 2))
        avtovaz_bought_pcs_label.configure(text=variables['avtovaz_bought_pcs'][0])

        aeroflot_price_label.configure(text=round(variables['aeroflot'][7], 2))
        aeroflot_bought_pcs_label.configure(text=variables['aeroflot_bought_pcs'][0])

        nornickel_price_label.configure(text=round(variables['nornickel'][7], 2))
        nornickel_bought_pcs_label.configure(text=variables['nornickel_bought_pcs'][0])

        lukoil_price_label.configure(text=round(variables['lukoil'][7], 2))
        lukoil_bought_pcs_label.configure(text=variables['lukoil_bought_pcs'][0])
        
        window_main.after(100, update)
    
    window_main=Tk()
    window_main.title('{} {} {} {} {} {}'.format('День', variables['day'][0], '|', 'Баланс:', round(variables['balance'][0], 2), 'RUB'))
    window_main.geometry('600x320')
    window_main.resizable(False, False)
    
    #Создание меню
    menu = Menu(window_main)
    window_main.config(menu=menu)

    mainmenu=Menu(menu, tearoff=0)
    mainmenu.add_command(label='О программе', command=about.init)
    mainmenu.add_command(label='Справка')
    mainmenu.add_separator()
    mainmenu.add_command(label='Следующий день', command=next_day.init)
    mainmenu.add_command(label='Сброс настроек', command=reset.init)
    mainmenu.add_separator()
    mainmenu.add_command(label='Выход из программы', command=window_main.quit)

    menu.add_cascade(label='Меню', menu=mainmenu)
    
    #Создание вкладок
    tabs = ttk.Notebook(window_main)
        
    tab_currency = ttk.Frame(tabs)
    tab_stocks = ttk.Frame(tabs)
    tab_raw = ttk.Frame(tabs)
        
    tabs.add(tab_currency, text='Валюта')
    tabs.add(tab_stocks, text='Акции')
    
    tabs.pack(expand=1, fill='both')

    #Интерфейс вкладки "Валюта"
    column1 = Label(tab_currency, text='Валюта', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(tab_currency, text='Покупка', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(tab_currency, text='Продажа', padx=5, pady=5)
    column3.grid(column=2, row=0)
    column4 = Label(tab_currency, text='Куплено', padx=5, pady=5)
    column4.grid(column=3, row=0)

    usd_label = Label(tab_currency, text='USD')
    usd_label.grid(column=0, row=1)
    usd_buy_label = Label(tab_currency, text=round(variables['usd_buy'][7], 2))
    usd_buy_label.grid(column=1, row=1)
    usd_sale_label = Label(tab_currency, text=round(variables['usd_sale'][7], 2))
    usd_sale_label.grid(column=2, row=1)
    usd_bought_label = Label(tab_currency, text=round(variables['usd_bought'][0], 2))
    usd_bought_label.grid(column=3, row=1)
    usd_details = Button(tab_currency, text=' ... ', command=window_details.usd)
    usd_details.grid(column=4, row=1)
    usd_purchasing = Button(tab_currency, text='Купить', command=window_buy.usd)
    usd_purchasing.grid(column=5, row=1)
    usd_selling = Button(tab_currency, text='Продать', command=window_sale.usd)
    usd_selling.grid(column=6, row=1)

    eur_label = Label(tab_currency, text='EUR')
    eur_label.grid(column=0, row=2)
    eur_buy_label = Label(tab_currency, text=round(variables['eur_buy'][7], 2))
    eur_buy_label.grid(column=1, row=2)
    eur_sale_label = Label(tab_currency, text=round(variables['eur_sale'][7], 2))
    eur_sale_label.grid(column=2, row=2)
    eur_bought_label = Label(tab_currency, text=round(variables['eur_bought'][0], 2))
    eur_bought_label.grid(column=3, row=2)
    eur_details = Button(tab_currency, text=' ... ', command=window_details.eur)
    eur_details.grid(column=4, row=2)
    eur_purchasing = Button(tab_currency, text='Купить', command=window_buy.eur)
    eur_purchasing.grid(column=5, row=2)
    eur_selling = Button(tab_currency, text='Продать', command=window_sale.eur)
    eur_selling.grid(column=6, row=2)

    chf_label = Label(tab_currency, text='CHF')
    chf_label.grid(column=0, row=3)
    chf_buy_label = Label(tab_currency, text=round(variables['chf_buy'][7], 2))
    chf_buy_label.grid(column=1, row=3)
    chf_sale_label = Label(tab_currency, text=round(variables['chf_sale'][7], 2))
    chf_sale_label.grid(column=2, row=3)
    chf_bought_label = Label(tab_currency, text=round(variables['chf_bought'][0], 2))
    chf_bought_label.grid(column=3, row=3)
    chf_details = Button(tab_currency, text=' ... ', command=window_details.chf)
    chf_details.grid(column=4, row=3)
    chf_purchasing = Button(tab_currency, text='Купить', command=window_buy.chf)
    chf_purchasing.grid(column=5, row=3)
    chf_selling = Button(tab_currency, text='Продать', command=window_sale.chf)
    chf_selling.grid(column=6, row=3)

    gbp_label = Label(tab_currency, text='GBP')
    gbp_label.grid(column=0, row=4)
    gbp_buy_label = Label(tab_currency, text=round(variables['gbp_buy'][7], 2))
    gbp_buy_label.grid(column=1, row=4)
    gbp_sale_label = Label(tab_currency, text=round(variables['gbp_sale'][7], 2))
    gbp_sale_label.grid(column=2, row=4)
    gbp_bought_label = Label(tab_currency, text=round(variables['gbp_bought'][0], 2))
    gbp_bought_label.grid(column=3, row=4)
    gbp_details = Button(tab_currency, text=' ... ', command=window_details.gbp)
    gbp_details.grid(column=4, row=4)
    gbp_purchasing = Button(tab_currency, text='Купить', command=window_buy.gbp)
    gbp_purchasing.grid(column=5, row=4)
    gbp_selling = Button(tab_currency, text='Продать', command=window_sale.gbp)
    gbp_selling.grid(column=6, row=4)

    jpy_label = Label(tab_currency, text='JPY')
    jpy_label.grid(column=0, row=5)
    jpy_buy_label = Label(tab_currency, text=round(variables['jpy_buy'][7], 2))
    jpy_buy_label.grid(column=1, row=5)
    jpy_sale_label = Label(tab_currency, text=round(variables['jpy_sale'][7], 2))
    jpy_sale_label.grid(column=2, row=5)
    jpy_bought_label = Label(tab_currency, text=round(variables['jpy_bought'][0], 2))
    jpy_bought_label.grid(column=3, row=5)
    jpy_details = Button(tab_currency, text=' ... ', command=window_details.jpy)
    jpy_details.grid(column=4, row=5)
    jpy_purchasing = Button(tab_currency, text='Купить', command=window_buy.jpy)
    jpy_purchasing.grid(column=5, row=5)
    jpy_selling = Button(tab_currency, text='Продать', command=window_sale.jpy)
    jpy_selling.grid(column=6, row=5)

    #Интерфейс вкладки "Акции"
    column1 = Label(tab_stocks, text='Компания/предприятие', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(tab_stocks, text='Цена', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(tab_stocks, text='Куплено (шт.)', padx=5, pady=5)
    column3.grid(column=2, row=0)
        
    gazprom_label = Label(tab_stocks, text='Gazprom')
    gazprom_label.grid(column=0, row=1)
    gazprom_price_label = Label(tab_stocks, text=round(variables['gazprom'][7], 2))
    gazprom_price_label.grid(column=1, row=1)
    gazprom_bought_pcs_label = Label(tab_stocks, text=variables['gazprom_bought_pcs'][0])
    gazprom_bought_pcs_label.grid(column=2, row=1)
    gazprom_details = Button(tab_stocks, text=' ... ', command=window_details.gazprom)
    gazprom_details.grid(column=3, row=1)
    gazprom_purchasing = Button(tab_stocks, text='Купить', command=window_buy.gazprom)
    gazprom_purchasing.grid(column=4, row=1)
    gazprom_selling = Button(tab_stocks, text='Продать', command=window_sale.gazprom)
    gazprom_selling.grid(column=5, row=1)

    avtovaz_label = Label(tab_stocks, text='Avtovaz')
    avtovaz_label.grid(column=0, row=2)
    avtovaz_price_label = Label(tab_stocks, text=round(variables['avtovaz'][7], 2))
    avtovaz_price_label.grid(column=1, row=2)
    avtovaz_bought_pcs_label = Label(tab_stocks, text=variables['avtovaz_bought_pcs'][0])
    avtovaz_bought_pcs_label.grid(column=2, row=2)
    avtovaz_details = Button(tab_stocks, text=' ... ', command=window_details.avtovaz)
    avtovaz_details.grid(column=3, row=2)
    avtovaz_purchasing = Button(tab_stocks, text='Купить', command=window_buy.avtovaz)
    avtovaz_purchasing.grid(column=4, row=2)
    avtovaz_selling = Button(tab_stocks, text='Продать', command=window_sale.avtovaz)
    avtovaz_selling.grid(column=5, row=2)

    aeroflot_label = Label(tab_stocks, text='Aeroflot')
    aeroflot_label.grid(column=0, row=3)
    aeroflot_price_label = Label(tab_stocks, text=round(variables['aeroflot'][7], 2))
    aeroflot_price_label.grid(column=1, row=3)
    aeroflot_bought_pcs_label = Label(tab_stocks, text=variables['aeroflot_bought_pcs'][0])
    aeroflot_bought_pcs_label.grid(column=2, row=3)
    aeroflot_details = Button(tab_stocks, text=' ... ', command=window_details.aeroflot)
    aeroflot_details.grid(column=3, row=3)
    aeroflot_purchasing = Button(tab_stocks, text='Купить', command=window_buy.aeroflot)
    aeroflot_purchasing.grid(column=4, row=3)
    aeroflot_selling = Button(tab_stocks, text='Продать', command=window_sale.aeroflot)
    aeroflot_selling.grid(column=5, row=3)

    nornickel_label = Label(tab_stocks, text='Nornickel')
    nornickel_label.grid(column=0, row=4)
    nornickel_price_label = Label(tab_stocks, text=round(variables['nornickel'][7], 2))
    nornickel_price_label.grid(column=1, row=4)
    nornickel_bought_pcs_label = Label(tab_stocks, text=variables['nornickel_bought_pcs'][0])
    nornickel_bought_pcs_label.grid(column=2, row=4)
    nornickel_details = Button(tab_stocks, text=' ... ', command=window_details.nornickel)
    nornickel_details.grid(column=3, row=4)
    nornickel_purchasing = Button(tab_stocks, text='Купить', command=window_buy.nornickel)
    nornickel_purchasing.grid(column=4, row=4)
    nornickel_selling = Button(tab_stocks, text='Продать', command=window_sale.nornickel)
    nornickel_selling.grid(column=5, row=4)

    lukoil_label = Label(tab_stocks, text='Lukoil')
    lukoil_label.grid(column=0, row=5)
    lukoil_price_label = Label(tab_stocks, text=round(variables['lukoil'][7], 2))
    lukoil_price_label.grid(column=1, row=5)
    lukoil_bought_pcs_label = Label(tab_stocks, text=variables['lukoil_bought_pcs'][0])
    lukoil_bought_pcs_label.grid(column=2, row=5)
    lukoil_details = Button(tab_stocks, text=' ... ', command=window_details.lukoil)
    lukoil_details.grid(column=3, row=5)
    lukoil_purchasing = Button(tab_stocks, text='Купить', command=window_buy.lukoil)
    lukoil_purchasing.grid(column=4, row=5)
    lukoil_selling = Button(tab_stocks, text='Продать', command=window_sale.lukoil)
    lukoil_selling.grid(column=5, row=5)

    update()
    
    window_main.mainloop()
#==========================================
