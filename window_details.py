#Модуль window_deails
#Запуск окон динамики цен

#Модули
from tkinter import *
import shelve
import random

#основная часть
variables = shelve.open('variables.dat')

#USD: Динамика курса
def usd():    
    usd_details=Toplevel()
    usd_details.title('USD: Динамика курса')
    usd_details.geometry('300x320')
    usd_details.resizable(False, False)

    column1 = Label(usd_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(usd_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(usd_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(usd_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(usd_details, text=round(variables['usd_buy'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(usd_details, text=round(variables['usd_buy'][7]-variables['usd_buy'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['usd_buy'][7]-variables['usd_buy'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['usd_buy'][7]-variables['usd_buy'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(usd_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(usd_details, text=round(variables['usd_buy'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(usd_details, text=round(variables['usd_buy'][6]-variables['usd_buy'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['usd_buy'][6]-variables['usd_buy'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['usd_buy'][6]-variables['usd_buy'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(usd_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(usd_details, text=round(variables['usd_buy'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(usd_details, text=round(variables['usd_buy'][5]-variables['usd_buy'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['usd_buy'][5]-variables['usd_buy'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['usd_buy'][5]-variables['usd_buy'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(usd_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(usd_details, text=round(variables['usd_buy'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(usd_details, text=round(variables['usd_buy'][4]-variables['usd_buy'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['usd_buy'][4]-variables['usd_buy'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['usd_buy'][4]-variables['usd_buy'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(usd_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(usd_details, text=round(variables['usd_buy'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(usd_details, text=round(variables['usd_buy'][3]-variables['usd_buy'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['usd_buy'][3]-variables['usd_buy'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['usd_buy'][3]-variables['usd_buy'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(usd_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(usd_details, text=round(variables['usd_buy'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(usd_details, text=round(variables['usd_buy'][2]-variables['usd_buy'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['usd_buy'][2]-variables['usd_buy'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['usd_buy'][2]-variables['usd_buy'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(usd_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(usd_details, text=round(variables['usd_buy'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(usd_details, text=round(variables['usd_buy'][1]-variables['usd_buy'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['usd_buy'][1]-variables['usd_buy'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['usd_buy'][1]-variables['usd_buy'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')
#EUR: Динамика курса
def eur():
    variables = shelve.open('variables.dat')
    
    eur_details=Toplevel()
    eur_details.title('EUR: Динамика курса')
    eur_details.geometry('300x320')
    eur_details.resizable(False, False)

    column1 = Label(eur_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(eur_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(eur_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(eur_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(eur_details, text=round(variables['eur_buy'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(eur_details, text=round(variables['eur_buy'][7]-variables['eur_buy'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['eur_buy'][7]-variables['eur_buy'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['eur_buy'][7]-variables['eur_buy'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(eur_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(eur_details, text=round(variables['eur_buy'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(eur_details, text=round(variables['eur_buy'][6]-variables['eur_buy'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['eur_buy'][6]-variables['eur_buy'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['eur_buy'][6]-variables['eur_buy'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(eur_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(eur_details, text=round(variables['eur_buy'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(eur_details, text=round(variables['eur_buy'][5]-variables['eur_buy'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['eur_buy'][5]-variables['eur_buy'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['eur_buy'][5]-variables['eur_buy'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(eur_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(eur_details, text=round(variables['eur_buy'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(eur_details, text=round(variables['eur_buy'][4]-variables['eur_buy'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['eur_buy'][4]-variables['eur_buy'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['eur_buy'][4]-variables['eur_buy'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(eur_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(eur_details, text=round(variables['eur_buy'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(eur_details, text=round(variables['eur_buy'][3]-variables['eur_buy'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['eur_buy'][3]-variables['eur_buy'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['eur_buy'][3]-variables['eur_buy'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(eur_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(eur_details, text=round(variables['eur_buy'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(eur_details, text=round(variables['eur_buy'][2]-variables['eur_buy'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['eur_buy'][2]-variables['eur_buy'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['eur_buy'][2]-variables['eur_buy'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(eur_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(eur_details, text=round(variables['eur_buy'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(eur_details, text=round(variables['eur_buy'][1]-variables['eur_buy'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['eur_buy'][1]-variables['eur_buy'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['eur_buy'][1]-variables['eur_buy'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#CHF: Динамика курса
def chf():
    variables = shelve.open('variables.dat')
    
    chf_details=Toplevel()
    chf_details.title('CHF: Динамика курса')
    chf_details.geometry('300x320')
    chf_details.resizable(False, False)

    column1 = Label(chf_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(chf_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(chf_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(chf_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(chf_details, text=round(variables['chf_buy'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(chf_details, text=round(variables['chf_buy'][7]-variables['chf_buy'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['chf_buy'][7]-variables['chf_buy'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['chf_buy'][7]-variables['chf_buy'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(chf_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(chf_details, text=round(variables['chf_buy'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(chf_details, text=round(variables['chf_buy'][6]-variables['chf_buy'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['chf_buy'][6]-variables['chf_buy'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['chf_buy'][6]-variables['chf_buy'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(chf_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(chf_details, text=round(variables['chf_buy'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(chf_details, text=round(variables['chf_buy'][5]-variables['chf_buy'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['chf_buy'][5]-variables['chf_buy'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['chf_buy'][5]-variables['chf_buy'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(chf_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(chf_details, text=round(variables['chf_buy'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(chf_details, text=round(variables['chf_buy'][4]-variables['chf_buy'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['chf_buy'][4]-variables['chf_buy'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['chf_buy'][4]-variables['chf_buy'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(chf_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(chf_details, text=round(variables['chf_buy'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(chf_details, text=round(variables['chf_buy'][3]-variables['chf_buy'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['chf_buy'][3]-variables['chf_buy'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['chf_buy'][3]-variables['chf_buy'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(chf_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(chf_details, text=round(variables['chf_buy'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(chf_details, text=round(variables['chf_buy'][2]-variables['chf_buy'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['chf_buy'][2]-variables['chf_buy'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['chf_buy'][2]-variables['chf_buy'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(chf_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(chf_details, text=round(variables['chf_buy'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(chf_details, text=round(variables['chf_buy'][1]-variables['chf_buy'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['chf_buy'][1]-variables['chf_buy'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['chf_buy'][1]-variables['chf_buy'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#GBP: Динамика курса
def gbp():
    variables = shelve.open('variables.dat')
    
    gbp_details=Toplevel()
    gbp_details.title('GBP: Динамика курса')
    gbp_details.geometry('300x320')
    gbp_details.resizable(False, False)

    column1 = Label(gbp_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(gbp_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(gbp_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(gbp_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(gbp_details, text=round(variables['gbp_buy'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(gbp_details, text=round(variables['gbp_buy'][7]-variables['gbp_buy'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['gbp_buy'][7]-variables['gbp_buy'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['gbp_buy'][7]-variables['gbp_buy'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(gbp_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(gbp_details, text=round(variables['gbp_buy'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(gbp_details, text=round(variables['gbp_buy'][6]-variables['gbp_buy'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['gbp_buy'][6]-variables['gbp_buy'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['gbp_buy'][6]-variables['gbp_buy'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(gbp_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][5]-variables['gbp_buy'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['gbp_buy'][5]-variables['gbp_buy'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['gbp_buy'][5]-variables['gbp_buy'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(gbp_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][4]-variables['gbp_buy'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['gbp_buy'][4]-variables['gbp_buy'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['gbp_buy'][4]-variables['gbp_buy'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(gbp_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][3]-variables['gbp_buy'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['gbp_buy'][3]-variables['gbp_buy'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['gbp_buy'][3]-variables['gbp_buy'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(gbp_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][2]-variables['gbp_buy'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['gbp_buy'][2]-variables['gbp_buy'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['gbp_buy'][2]-variables['gbp_buy'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(gbp_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(gbp_details, text=round(variables['gbp_buy'][1]-variables['gbp_buy'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['gbp_buy'][1]-variables['gbp_buy'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['gbp_buy'][1]-variables['gbp_buy'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#JPY: Динамика курса
def jpy():
    variables = shelve.open('variables.dat')
    
    jpy_details=Toplevel()
    jpy_details.title('JPY: Динамика курса')
    jpy_details.geometry('300x320')
    jpy_details.resizable(False, False)

    column1 = Label(jpy_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(jpy_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(jpy_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(jpy_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(jpy_details, text=round(variables['jpy_buy'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(jpy_details, text=round(variables['jpy_buy'][7]-variables['jpy_buy'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['jpy_buy'][7]-variables['jpy_buy'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['jpy_buy'][7]-variables['jpy_buy'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(jpy_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(jpy_details, text=round(variables['jpy_buy'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(jpy_details, text=round(variables['jpy_buy'][6]-variables['jpy_buy'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['jpy_buy'][6]-variables['jpy_buy'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['jpy_buy'][6]-variables['jpy_buy'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(jpy_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][5]-variables['jpy_buy'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['jpy_buy'][5]-variables['jpy_buy'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['jpy_buy'][5]-variables['jpy_buy'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(jpy_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][4]-variables['jpy_buy'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['jpy_buy'][4]-variables['jpy_buy'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['jpy_buy'][4]-variables['jpy_buy'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(jpy_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][3]-variables['jpy_buy'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['jpy_buy'][3]-variables['jpy_buy'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['jpy_buy'][3]-variables['jpy_buy'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(jpy_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][2]-variables['jpy_buy'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['jpy_buy'][2]-variables['jpy_buy'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['jpy_buy'][2]-variables['jpy_buy'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(jpy_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(jpy_details, text=round(variables['jpy_buy'][1]-variables['jpy_buy'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['jpy_buy'][1]-variables['jpy_buy'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['jpy_buy'][1]-variables['jpy_buy'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#Gazprom: Динамика цен
def gazprom():
    variables = shelve.open('variables.dat')
    
    gazprom_details=Toplevel()
    gazprom_details.title('Gazprom: Динамика цен')
    gazprom_details.geometry('300x320')
    gazprom_details.resizable(False, False)

    column1 = Label(gazprom_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(gazprom_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(gazprom_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(gazprom_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(gazprom_details, text=round(variables['gazprom'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(gazprom_details, text=round(variables['gazprom'][7]-variables['gazprom'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['gazprom'][7]-variables['gazprom'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['gazprom'][7]-variables['gazprom'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(gazprom_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(gazprom_details, text=round(variables['gazprom'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(gazprom_details, text=round(variables['gazprom'][6]-variables['gazprom'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['gazprom'][6]-variables['gazprom'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['gazprom'][6]-variables['gazprom'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(gazprom_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(gazprom_details, text=round(variables['gazprom'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(gazprom_details, text=round(variables['gazprom'][5]-variables['gazprom'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['gazprom'][5]-variables['gazprom'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['gazprom'][5]-variables['gazprom'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(gazprom_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(gazprom_details, text=round(variables['gazprom'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(gazprom_details, text=round(variables['gazprom'][4]-variables['gazprom'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['gazprom'][4]-variables['gazprom'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['gazprom'][4]-variables['gazprom'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(gazprom_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(gazprom_details, text=round(variables['gazprom'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(gazprom_details, text=round(variables['gazprom'][3]-variables['gazprom'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['gazprom'][3]-variables['gazprom'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['gazprom'][3]-variables['gazprom'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(gazprom_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(gazprom_details, text=round(variables['gazprom'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(gazprom_details, text=round(variables['gazprom'][2]-variables['gazprom'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['gazprom'][2]-variables['gazprom'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['gazprom'][2]-variables['gazprom'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(gazprom_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(gazprom_details, text=round(variables['gazprom'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(gazprom_details, text=round(variables['gazprom'][1]-variables['gazprom'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['gazprom'][1]-variables['gazprom'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['gazprom'][1]-variables['gazprom'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#Avtovaz: Динамика цен
def avtovaz():
    variables = shelve.open('variables.dat')
    
    avtovaz_details=Toplevel()
    avtovaz_details.title('Avtovaz: Динамика цен')
    avtovaz_details.geometry('300x320')
    avtovaz_details.resizable(False, False)

    column1 = Label(avtovaz_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(avtovaz_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(avtovaz_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(avtovaz_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(avtovaz_details, text=round(variables['avtovaz'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(avtovaz_details, text=round(variables['avtovaz'][7]-variables['avtovaz'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['avtovaz'][7]-variables['avtovaz'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['avtovaz'][7]-variables['avtovaz'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(avtovaz_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(avtovaz_details, text=round(variables['avtovaz'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(avtovaz_details, text=round(variables['avtovaz'][6]-variables['avtovaz'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['avtovaz'][6]-variables['avtovaz'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['avtovaz'][6]-variables['avtovaz'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(avtovaz_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][5]-variables['avtovaz'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['avtovaz'][5]-variables['avtovaz'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['avtovaz'][5]-variables['avtovaz'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(avtovaz_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][4]-variables['avtovaz'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['avtovaz'][4]-variables['avtovaz'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['avtovaz'][4]-variables['avtovaz'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(avtovaz_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][3]-variables['avtovaz'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['avtovaz'][3]-variables['avtovaz'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['avtovaz'][3]-variables['avtovaz'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(avtovaz_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][2]-variables['avtovaz'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['avtovaz'][2]-variables['avtovaz'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['avtovaz'][2]-variables['avtovaz'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(avtovaz_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(avtovaz_details, text=round(variables['avtovaz'][1]-variables['avtovaz'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['avtovaz'][1]-variables['avtovaz'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['avtovaz'][1]-variables['avtovaz'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#Aeroflot: Динамика цен
def aeroflot():
    variables = shelve.open('variables.dat')
    
    aeroflot_details=Toplevel()
    aeroflot_details.title('Aeroflot: Динамика цен')
    aeroflot_details.geometry('300x320')
    aeroflot_details.resizable(False, False)

    column1 = Label(aeroflot_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(aeroflot_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(aeroflot_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(aeroflot_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(aeroflot_details, text=round(variables['aeroflot'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(aeroflot_details, text=round(variables['aeroflot'][7]-variables['aeroflot'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['aeroflot'][7]-variables['aeroflot'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['aeroflot'][7]-variables['aeroflot'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(aeroflot_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(aeroflot_details, text=round(variables['aeroflot'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(aeroflot_details, text=round(variables['aeroflot'][6]-variables['aeroflot'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['aeroflot'][6]-variables['aeroflot'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['aeroflot'][6]-variables['aeroflot'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(aeroflot_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][5]-variables['aeroflot'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['aeroflot'][5]-variables['aeroflot'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['aeroflot'][5]-variables['aeroflot'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(aeroflot_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][4]-variables['aeroflot'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['aeroflot'][4]-variables['aeroflot'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['aeroflot'][4]-variables['aeroflot'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(aeroflot_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][3]-variables['aeroflot'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['aeroflot'][3]-variables['aeroflot'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['aeroflot'][3]-variables['aeroflot'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(aeroflot_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][2]-variables['aeroflot'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['aeroflot'][2]-variables['aeroflot'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['aeroflot'][2]-variables['aeroflot'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(aeroflot_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(aeroflot_details, text=round(variables['aeroflot'][1]-variables['aeroflot'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['aeroflot'][1]-variables['aeroflot'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['aeroflot'][1]-variables['aeroflot'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#Nornickel: Динамика цен
def nornickel():
    variables = shelve.open('variables.dat')
    
    nornickel_details=Toplevel()
    nornickel_details.title('Nornickel: Динамика цен')
    nornickel_details.geometry('300x320')
    nornickel_details.resizable(False, False)

    column1 = Label(nornickel_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(nornickel_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(nornickel_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(nornickel_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(nornickel_details, text=round(variables['nornickel'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(nornickel_details, text=round(variables['nornickel'][7]-variables['nornickel'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['nornickel'][7]-variables['nornickel'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['nornickel'][7]-variables['nornickel'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(nornickel_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(nornickel_details, text=round(variables['nornickel'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(nornickel_details, text=round(variables['nornickel'][6]-variables['nornickel'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['nornickel'][6]-variables['nornickel'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['nornickel'][6]-variables['nornickel'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(nornickel_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(nornickel_details, text=round(variables['nornickel'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(nornickel_details, text=round(variables['nornickel'][5]-variables['nornickel'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['nornickel'][5]-variables['nornickel'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['nornickel'][5]-variables['nornickel'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(nornickel_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(nornickel_details, text=round(variables['nornickel'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(nornickel_details, text=round(variables['nornickel'][4]-variables['nornickel'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['nornickel'][4]-variables['nornickel'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['nornickel'][4]-variables['nornickel'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(nornickel_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(nornickel_details, text=round(variables['nornickel'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(nornickel_details, text=round(variables['nornickel'][3]-variables['nornickel'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['nornickel'][3]-variables['nornickel'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['nornickel'][3]-variables['nornickel'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(nornickel_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(nornickel_details, text=round(variables['nornickel'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(nornickel_details, text=round(variables['nornickel'][2]-variables['nornickel'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['nornickel'][2]-variables['nornickel'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['nornickel'][2]-variables['nornickel'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(nornickel_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(nornickel_details, text=round(variables['nornickel'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(nornickel_details, text=round(variables['nornickel'][1]-variables['nornickel'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['nornickel'][1]-variables['nornickel'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['nornickel'][1]-variables['nornickel'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')

#Lukoil: Динамика цен
def lukoil():
    variables = shelve.open('variables.dat')
    
    lukoil_details=Toplevel()
    lukoil_details.title('Lukoil: Динамика цен')
    lukoil_details.geometry('300x320')
    lukoil_details.resizable(False, False)

    column1 = Label(lukoil_details, text='День', padx=5, pady=5)
    column1.grid(column=0, row=0)
    column2 = Label(lukoil_details, text='Курс', padx=5, pady=5)
    column2.grid(column=1, row=0)
    column3 = Label(lukoil_details, text='Изменение', padx=5, pady=5)
    column3.grid(column=2, row=0)
    
    today = Label(lukoil_details, text=variables['day'][0])
    today.grid(column=0, row=1)
    rate_today = Label(lukoil_details, text=round(variables['lukoil'][7], 2))
    rate_today.grid(column=1, row=1)
    change_today = Label(lukoil_details, text=round(variables['lukoil'][7]-variables['lukoil'][6], 2))
    change_today.grid(column=2, row=1)
    if round(variables['lukoil'][7]-variables['lukoil'][6], 2) < 0:
        change_today.configure(fg='red')
    if round(variables['lukoil'][7]-variables['lukoil'][6], 2) > 0:
        change_today.configure(fg='green')

    yesterday = Label(lukoil_details, text=variables['day'][0]-1)
    yesterday.grid(column=0, row=2)
    rate_yesterday = Label(lukoil_details, text=round(variables['lukoil'][6], 2))
    rate_yesterday.grid(column=1, row=2)
    change_yesterday = Label(lukoil_details, text=round(variables['lukoil'][6]-variables['lukoil'][5], 2))
    change_yesterday.grid(column=2, row=2)
    if round(variables['lukoil'][6]-variables['lukoil'][5], 2) < 0:
        change_yesterday.configure(fg='red')
    if round(variables['lukoil'][6]-variables['lukoil'][5], 2) > 0:
        change_yesterday.configure(fg='green')

    two_days_ago = Label(lukoil_details, text=variables['day'][0]-2)
    two_days_ago.grid(column=0, row=3)
    rate_two_days_ago = Label(lukoil_details, text=round(variables['lukoil'][5], 2))
    rate_two_days_ago.grid(column=1, row=3)
    change_two_days_ago = Label(lukoil_details, text=round(variables['lukoil'][5]-variables['lukoil'][4], 2))
    change_two_days_ago.grid(column=2, row=3)
    if round(variables['lukoil'][5]-variables['lukoil'][4], 2) < 0:
        change_two_days_ago.configure(fg='red')
    if round(variables['lukoil'][5]-variables['lukoil'][4], 2) > 0:
        change_two_days_ago.configure(fg='green')

    three_days_ago = Label(lukoil_details, text=variables['day'][0]-3)
    three_days_ago.grid(column=0, row=4)
    rate_three_days_ago = Label(lukoil_details, text=round(variables['lukoil'][4], 2))
    rate_three_days_ago.grid(column=1, row=4)
    change_three_days_ago = Label(lukoil_details, text=round(variables['lukoil'][4]-variables['lukoil'][3], 2))
    change_three_days_ago.grid(column=2, row=4)
    if round(variables['lukoil'][4]-variables['lukoil'][3], 2) < 0:
        change_three_days_ago.configure(fg='red')
    if round(variables['lukoil'][4]-variables['lukoil'][3], 2) > 0:
        change_three_days_ago.configure(fg='green')

    four_days_ago = Label(lukoil_details, text=variables['day'][0]-4)
    four_days_ago.grid(column=0, row=5)
    rate_four_days_ago = Label(lukoil_details, text=round(variables['lukoil'][3], 2))
    rate_four_days_ago.grid(column=1, row=5)
    change_four_days_ago = Label(lukoil_details, text=round(variables['lukoil'][3]-variables['lukoil'][2], 2))
    change_four_days_ago.grid(column=2, row=5)
    if round(variables['lukoil'][3]-variables['lukoil'][2], 2) < 0:
        change_four_days_ago.configure(fg='red')
    if round(variables['lukoil'][3]-variables['lukoil'][2], 2) > 0:
        change_four_days_ago.configure(fg='green')

    five_days_ago = Label(lukoil_details, text=variables['day'][0]-5)
    five_days_ago.grid(column=0, row=6)
    rate_five_days_ago = Label(lukoil_details, text=round(variables['lukoil'][2], 2))
    rate_five_days_ago.grid(column=1, row=6)
    change_five_days_ago = Label(lukoil_details, text=round(variables['lukoil'][2]-variables['lukoil'][1], 2))
    change_five_days_ago.grid(column=2, row=6)
    if round(variables['lukoil'][2]-variables['lukoil'][1], 2) < 0:
        change_five_days_ago.configure(fg='red')
    if round(variables['lukoil'][2]-variables['lukoil'][1], 2) > 0:
        change_five_days_ago.configure(fg='green')

    six_days_ago = Label(lukoil_details, text=variables['day'][0]-6)
    six_days_ago.grid(column=0, row=7)
    rate_six_days_ago = Label(lukoil_details, text=round(variables['lukoil'][1], 2))
    rate_six_days_ago.grid(column=1, row=7)
    change_six_days_ago = Label(lukoil_details, text=round(variables['lukoil'][1]-variables['lukoil'][0], 2))
    change_six_days_ago.grid(column=2, row=7)
    if round(variables['lukoil'][1]-variables['lukoil'][0], 2) < 0:
        change_six_days_ago.configure(fg='red')
    if round(variables['lukoil'][1]-variables['lukoil'][0], 2) > 0:
        change_six_days_ago.configure(fg='green')
