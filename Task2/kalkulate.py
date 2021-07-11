import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()      #принимаем значение на входе
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc['state']=tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
    calc['state']=tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '-' in value or '+' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state']=tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)
    calc['state']=tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value+value[:-1]
    calc['state']=tk.NORMAL
    calc.delete(0,tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Увага','Можливо введення тільки цифр та математичних операций!')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Увага','На 0 ділити заборонено!')
        calc.insert(0,0)
    calc['state']=tk.DISABLED


def clear():
    calc['state']=tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,0)
    calc['state']=tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, font=('Arial',12), command=lambda : add_digit(digit))#функция создания кнопки


def make_operation_button(operation):
    return tk.Button(text=operation, font=('Arial',12),
                     command=lambda : add_operation(operation))#функция создания мат. операции


def make_calc_button(operation):
    return tk.Button(text=operation, font=('Arial',12),
                     command=calculate)#функция создания мат. операции


def make_clear_button(operation):
    return tk.Button(text=operation, font=('Arial',12),
                     command=clear)# очистка 


def press_key(event):    #функция проверки и вывода цифр и операций с клав.
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char =='\r':
        calculate()


win = tk.Tk()
win.iconbitmap("testicon.ico")  #обявление иконки 
win.config(bg='silver')         #цвет бэкграунда
win.attributes('-alpha', 0.95)  #прозрасность
win.title('Калькулятор')        #имя окна
win.geometry("240x270+10+15")   #размер и кординаты окна относительно левого верхнего края
win.resizable(False, False)     #запрет на манипуляции размера

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15),width=15,)      #настройки ( шрифт и т.п.)
calc.insert(0,'0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, stick='we')    #обьявление поля вывода; растягивание 

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)      #обьявление кнопок и их координаты.
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)      #примечание - lambda команда для команд 
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=1, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=0, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0,minsize=60)      #отступ лева право
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)     #отступ снизу сверху 
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)

win.mainloop()
