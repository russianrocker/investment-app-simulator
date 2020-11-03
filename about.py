#Модуль about
#Окно "О программе"

#Модули
from tkinter import *
from tkinter import ttk

#Основная часть
def init():
    about = Toplevel()
    about.title('О программе')
    about.geometry('250x240')
    about.resizable(False, False)

    canvas = Canvas(about, width=128, height=128)
    canvas.grid(column=0, row=0)
    icon = PhotoImage(file='icon.png')
    canvas.create_image(0, 0, anchor='nw', image=icon)

    separator = ttk.Separator(about, orient=HORIZONTAL)
    separator.grid(column=0, row=1, sticky='we', padx=5)

    program_name = Label(about, text='Симулятор инвест-приложения')
    program_name.grid(column=0, row=2, sticky='nw')

    version = Label(about, text='Версия: 0.1 beta')
    version.grid(column=0, row=3, sticky='nw')

    developer = Label(about, text='Разработчик: Виктор К.')
    developer.grid(column=0, row=4, sticky='nw')

    about.mainloop()
