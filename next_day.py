#Модуль next_day

from tkinter import *
from tkinter import messagebox
import shelve
import random

spread = round(random.random(), 2)

def init():
    variables = shelve.open('variables.dat')

    new_day = variables['day'][0] + 1
    variables['day'] = [new_day]

    variables['usd_buy'] = [variables['usd_buy'][1], variables['usd_buy'][2],
                            variables['usd_buy'][3], variables['usd_buy'][4],
                            variables['usd_buy'][5], variables['usd_buy'][6],
                            variables['usd_buy'][7], variables['usd_buy'][7]+round(random.uniform(-0.50, 0.50), 2)]
    variables['eur_buy'] = [variables['eur_buy'][1], variables['eur_buy'][2],
                            variables['eur_buy'][3], variables['eur_buy'][4],
                            variables['eur_buy'][5], variables['eur_buy'][6],
                            variables['eur_buy'][7], variables['eur_buy'][7]+round(random.uniform(-0.50, 0.50), 2)]
    variables['chf_buy'] = [variables['chf_buy'][1], variables['chf_buy'][2],
                            variables['chf_buy'][3], variables['chf_buy'][4],
                            variables['chf_buy'][5], variables['chf_buy'][6],
                            variables['chf_buy'][7], variables['chf_buy'][7]+round(random.uniform(-0.50, 0.50), 2)]
    variables['gbp_buy'] = [variables['gbp_buy'][1], variables['gbp_buy'][2],
                            variables['gbp_buy'][3], variables['gbp_buy'][4],
                            variables['gbp_buy'][5], variables['gbp_buy'][6],
                            variables['gbp_buy'][7], variables['gbp_buy'][7]+round(random.uniform(-0.50, 0.50), 2)]
    variables['jpy_buy'] = [variables['jpy_buy'][1], variables['jpy_buy'][2],
                            variables['jpy_buy'][3], variables['jpy_buy'][4],
                            variables['jpy_buy'][5], variables['jpy_buy'][6],
                            variables['jpy_buy'][7], variables['jpy_buy'][7]+round(random.uniform(-0.50, 0.50), 2)]

    variables['usd_sale'] = [variables['usd_sale'][1], variables['usd_sale'][2],
                            variables['usd_sale'][3], variables['usd_sale'][4],
                            variables['usd_sale'][5], variables['usd_sale'][6],
                            variables['usd_sale'][7], variables['usd_buy'][7]+round(spread, 2)]
    variables['eur_sale'] = [variables['eur_sale'][1], variables['eur_sale'][2],
                            variables['eur_sale'][3], variables['eur_sale'][4],
                            variables['eur_sale'][5], variables['eur_sale'][6],
                            variables['eur_sale'][7], variables['eur_buy'][7]+round(spread, 2)]
    variables['chf_sale'] = [variables['chf_sale'][1], variables['chf_sale'][2],
                            variables['chf_sale'][3], variables['chf_sale'][4],
                            variables['chf_sale'][5], variables['chf_sale'][6],
                            variables['chf_sale'][7], variables['chf_buy'][7]+round(spread, 2)]
    variables['gbp_sale'] = [variables['gbp_sale'][1], variables['gbp_sale'][2],
                            variables['gbp_sale'][3], variables['gbp_sale'][4],
                            variables['gbp_sale'][5], variables['gbp_sale'][6],
                            variables['gbp_sale'][7], variables['gbp_buy'][7]+round(spread, 2)]
    variables['jpy_sale'] = [variables['jpy_sale'][1], variables['jpy_sale'][2],
                            variables['jpy_sale'][3], variables['jpy_sale'][4],
                            variables['jpy_sale'][5], variables['jpy_sale'][6],
                            variables['jpy_sale'][7], variables['jpy_buy'][7]+round(spread, 2)]

    variables['gazprom'] = [variables['gazprom'][1], variables['gazprom'][2],
                            variables['gazprom'][3], variables['gazprom'][4],
                            variables['gazprom'][5], variables['gazprom'][6],
                            variables['gazprom'][7], variables['gazprom'][7]+round(random.uniform(-2.50, 2.50), 2)]
    variables['avtovaz'] = [variables['avtovaz'][1], variables['avtovaz'][2],
                            variables['avtovaz'][3], variables['avtovaz'][4],
                            variables['avtovaz'][5], variables['avtovaz'][6],
                            variables['avtovaz'][7], variables['avtovaz'][7]+round(random.uniform(-2.50, 2.50), 2)]
    variables['aeroflot'] = [variables['aeroflot'][1], variables['aeroflot'][2],
                            variables['aeroflot'][3], variables['aeroflot'][4],
                            variables['aeroflot'][5], variables['aeroflot'][6],
                            variables['aeroflot'][7], variables['aeroflot'][7]+round(random.uniform(-2.50, 2.50), 2)]
    variables['nornickel'] = [variables['nornickel'][1], variables['nornickel'][2],
                            variables['nornickel'][3], variables['nornickel'][4],
                            variables['nornickel'][5], variables['nornickel'][6],
                            variables['nornickel'][7], variables['nornickel'][7]+round(random.uniform(-2.50, 2.50), 2)]
    variables['lukoil'] = [variables['lukoil'][1], variables['lukoil'][2],
                            variables['lukoil'][3], variables['lukoil'][4],
                            variables['lukoil'][5], variables['lukoil'][6],
                            variables['lukoil'][7], variables['lukoil'][7]+round(random.uniform(-2.50, 2.50), 2)]

    messagebox.showinfo('', '{} {}'.format('День', variables['day'][0]))
