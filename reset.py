#Модуль reset
#Производит сброс программы

from tkinter import *
from tkinter import messagebox
import shelve
import random

balance = [50000]
spread = random.random()
day = [1]

#ВАЛЮТА
#Цены покупки валют
usd_buy = [60.67, 60.73, 60.56, 60.45, 60.54, 60.62, 60.65, 60.58]
eur_buy = [69.38, 69.35, 69.42, 69.49, 69.52, 69.48, 60.46, 60.55]
chf_buy = [64.95, 64.92, 64.82, 64.87, 69.91, 69.97, 69.99, 69.96]
gbp_buy = [80.24, 80.21, 80.17, 80.12, 80.09, 80.13, 80.19, 80.23]
jpy_buy = [60.03, 60.09, 60.02, 60.07, 60.11, 60.17, 60.14, 60.12]

#Цены продажи валют
usd_sale = [usd_buy[0]+round(spread, 2), usd_buy[1]+round(spread, 2), usd_buy[2]+round(spread, 2), usd_buy[3]+round(spread, 2), usd_buy[4]+round(spread, 2), usd_buy[5]+round(spread, 2), usd_buy[6]+round(spread, 2), usd_buy[7]+round(spread, 2)]
eur_sale = [eur_buy[0]+round(spread, 2), eur_buy[1]+round(spread, 2), eur_buy[2]+round(spread, 2), eur_buy[3]+round(spread, 2), eur_buy[4]+round(spread, 2), eur_buy[5]+round(spread, 2), eur_buy[6]+round(spread, 2), eur_buy[7]+round(spread, 2)]
chf_sale = [chf_buy[0]+round(spread, 2), chf_buy[1]+round(spread, 2), chf_buy[2]+round(spread, 2), chf_buy[3]+round(spread, 2), chf_buy[4]+round(spread, 2), chf_buy[5]+round(spread, 2), chf_buy[6]+round(spread, 2), chf_buy[7]+round(spread, 2)]
gbp_sale = [gbp_buy[0]+round(spread, 2), gbp_buy[1]+round(spread, 2), gbp_buy[2]+round(spread, 2), gbp_buy[3]+round(spread, 2), gbp_buy[4]+round(spread, 2), gbp_buy[5]+round(spread, 2), gbp_buy[6]+round(spread, 2), gbp_buy[7]+round(spread, 2)]
jpy_sale = [jpy_buy[0]+round(spread, 2), jpy_buy[1]+round(spread, 2), jpy_buy[2]+round(spread, 2), jpy_buy[3]+round(spread, 2), jpy_buy[4]+round(spread, 2), jpy_buy[5]+round(spread, 2), jpy_buy[6]+round(spread, 2), jpy_buy[7]+round(spread, 2)]

#Куплено валюты
usd_bought = [0.00]
eur_bought = [0.00]
chf_bought = [0.00]
gbp_bought = [0.00]
jpy_bought = [0.00]

#АКЦИИ
#Цены на акции
gazprom = [254.95, 254.12, 253.83, 255.11, 256.76, 257.24, 256.45, 257.75]
avtovaz = [11.07, 11.53, 12.28, 14.04, 15.89, 16.54, 15.56, 15.81]
aeroflot = [109.02, 108.45, 109.11, 110.62, 111.97, 113.71, 112.17, 111.35]
nornickel = [20903.84, 20903.14, 20904.84, 20906.06, 20905.24, 20906.88, 20908.59, 20907.25]
lukoil = [6682.19, 6682.98, 6684.83, 6683.19, 6682.37, 6681.48, 6680.93, 6682.41]

#Количество купленных акций
gazprom_bought_pcs = [0]
avtovaz_bought_pcs = [0]
aeroflot_bought_pcs = [0]
nornickel_bought_pcs = [0]
lukoil_bought_pcs = [0]

def init():
    consent_to_reset = messagebox.askyesno('Предупреждение', 'Сбросить настройки программы? Текущий прогресс будет утрачен БЕЗВОЗВРАТНО!')
    
    if consent_to_reset == True:
        variables = shelve.open('variables.dat')
        
        variables['balance'] = [50000]
        variables['day'] = [1]
        
        variables['usd_buy'] = [60.67, 60.73, 60.56, 60.45, 60.54, 60.62, 60.65, 60.58]
        variables['eur_buy'] = [69.38, 69.35, 69.42, 69.49, 69.52, 69.48, 60.46, 60.55]
        variables['chf_buy'] = [64.95, 64.92, 64.82, 64.87, 69.91, 69.97, 69.99, 69.96]
        variables['gbp_buy'] = [80.24, 80.21, 80.17, 80.12, 80.09, 80.13, 80.19, 80.23]
        variables['jpy_buy'] = [60.03, 60.09, 60.02, 60.07, 60.11, 60.17, 60.14, 60.12]

        variables['usd_sale'] = [usd_buy[0]+round(spread, 2), usd_buy[1]+round(spread, 2), usd_buy[2]+round(spread, 2), usd_buy[3]+round(spread, 2), usd_buy[4]+round(spread, 2), usd_buy[5]+round(spread, 2), usd_buy[6]+round(spread, 2), usd_buy[7]+round(spread, 2)]
        variables['eur_sale'] = [eur_buy[0]+round(spread, 2), eur_buy[1]+round(spread, 2), eur_buy[2]+round(spread, 2), eur_buy[3]+round(spread, 2), eur_buy[4]+round(spread, 2), eur_buy[5]+round(spread, 2), eur_buy[6]+round(spread, 2), eur_buy[7]+round(spread, 2)]
        variables['chf_sale'] = [chf_buy[0]+round(spread, 2), chf_buy[1]+round(spread, 2), chf_buy[2]+round(spread, 2), chf_buy[3]+round(spread, 2), chf_buy[4]+round(spread, 2), chf_buy[5]+round(spread, 2), chf_buy[6]+round(spread, 2), chf_buy[7]+round(spread, 2)]
        variables['gbp_sale'] = [gbp_buy[0]+round(spread, 2), gbp_buy[1]+round(spread, 2), gbp_buy[2]+round(spread, 2), gbp_buy[3]+round(spread, 2), gbp_buy[4]+round(spread, 2), gbp_buy[5]+round(spread, 2), gbp_buy[6]+round(spread, 2), gbp_buy[7]+round(spread, 2)]
        variables['jpy_sale'] = [jpy_buy[0]+round(spread, 2), jpy_buy[1]+round(spread, 2), jpy_buy[2]+round(spread, 2), jpy_buy[3]+round(spread, 2), jpy_buy[4]+round(spread, 2), jpy_buy[5]+round(spread, 2), jpy_buy[6]+round(spread, 2), jpy_buy[7]+round(spread, 2)]

        variables['usd_bought'] = [0.00]
        variables['eur_bought'] = [0.00]
        variables['chf_bought'] = [0.00]
        variables['gbp_bought'] = [0.00]
        variables['jpy_bought'] = [0.00]

        variables['gazprom'] = [254.95, 254.12, 253.83, 255.11, 256.76, 257.24, 256.45, 257.75]
        variables['avtovaz'] = [11.07, 11.53, 12.28, 14.04, 15.89, 16.54, 15.56, 15.81]
        variables['aeroflot'] = [109.02, 108.45, 109.11, 110.62, 111.97, 113.71, 112.17, 111.35]
        variables['nornickel'] = [20903.84, 20903.14, 20904.84, 20906.06, 20905.24, 20906.88, 20908.59, 20907.25]
        variables['lukoil'] = [6682.19, 6682.98, 6684.83, 6683.19, 6682.37, 6681.48, 6680.93, 6682.41]

        variables['gazprom_bought_pcs'] = [0]
        variables['avtovaz_bought_pcs'] = [0]
        variables['aeroflot_bought_pcs'] = [0]
        variables['nornickel_bought_pcs'] = [0]
        variables['lukoil_bought_pcs'] = [0]

        variables.sync()
        variables.close()

if __name__ == '__main__':
    init()
