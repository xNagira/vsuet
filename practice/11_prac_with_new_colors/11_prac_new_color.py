from tkinter import*
from tkinter import ttk, messagebox, filedialog

window = Tk()
window.title('Морозова Яна Евгеньевна')
window.geometry('720x400')

tab1 = None
tab2 = None
tab3 = None
n1 = None
n2 = None
r = None
tx = None
v1 = None
v2 = None
v3 = None

def prog():
    global tab1, tab2, tab3
    tab_control = ttk.Notebook(window)

    tab1 = ttk.Frame(tab_control, style='TFrame')
    tab_control.add(tab1, text='Калькулятор')
    calculator()

    tab2 = ttk.Frame(tab_control, style='TFrame')
    tab_control.add(tab2, text='Чекбоксы')
    boxes()

    tab3 = ttk.Frame(tab_control, style='TFrame')
    tab_control.add(tab3, text='Работа с текстом')
    text_work()

    tab_control.pack(expand=1, fill='both')
    tab_control.tab(tab1, padding=(10, 10))
    tab_control.tab(tab2, padding=(10, 10))
    tab_control.tab(tab3, padding=(10, 10))

    style = ttk.Style()
    style.theme_use('default')
    style.configure("TFrame", background="#F8F6F7")
    style.configure("TLabel", background="#2B3B60")
    style.configure("TButton", background="#2B3B60")


    style.configure("TNotebook", background="#384F80", foreground="#2B3B60")
    style.configure("TNotebook.Tab", background="#384F80", foreground="#F7F6F7")
    style.map("TNotebook.Tab", background=[("selected", "#384F80"), ("active", "#4E66A5")],
              foreground=[("selected", "#F7F6F7"), ("active", "white")])

def calculator():
    global n1, n2, r
    n1 = DoubleVar()
    n2 = DoubleVar()
    r = StringVar()

    lbl1 = Label(tab1, text='Первое число:', background='#C7D2CC',font=("Arial Bold", 10), fg="#2B3B60")
    lbl1.grid(column=0, row=0)
    lbl21 = Entry(tab1, textvariable=n1)
    lbl21.grid(row=0, column=1)

    lbl3 = Label(tab1, text='Операция:', background='#C7D2CC',font=("Arial Bold", 10), fg="#2B3B60")
    lbl3.grid(row=1, column=0)
    combo = ttk.Combobox(tab1)
    combo['values'] = ('+', '-', '*', '/')
    combo.grid(column=1, row=1)

    lbl4 = Label(tab1, text='Второе число:', background='#C7D2CC', font=("Arial Bold", 10), fg="#2B3B60")
    lbl4.grid(column=0, row=2)
    lbl41 = Entry(tab1, textvariable=n2)
    lbl41.grid(row=2, column=1)

    btn = Button(tab1, text='Посчитать', command=lambda: calculat(combo), font=("Arial Bold", 10), fg="#2B3B60", background='#C7D2CC')
    btn.grid(column=3, row=1)

    btnn = Label(tab1, text='Результат:', background='#C7D2CC',font=("Arial Bold", 10), fg="#2B3B60")
    btnn.grid(row=5, column=0)
    res = Label(tab1, textvariable=r, background="#F8F6F7", fg="#6a1b9a")
    res.grid(row=5, column=1)

def calculat(combo):
    try:
        nu1 = n1.get()
        nu2 = n2.get()
        oper = combo.get()
        if oper == '+':
            r.set(nu1 + nu2)
        elif oper == '-':
            r.set(nu1 - nu2)
        elif oper == '*':
            r.set(nu1 * nu2)
        elif oper == '/':
            if nu2 != 0:
                r.set(nu1 / nu2)
            else:
                r.set('Ошибка: деление на ноль')
        else:
            r.set('Выберите операцию')
    except Exception:
        r.set("Ошибка")

def boxes():
    global v1, v2, v3
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()

    chk = Checkbutton(tab2, text='Первый', variable=v1, background='#C7D2CC', font=("Arial Bold", 10), fg="#2B3B60")
    chk.grid(column=0, row=0)
    chk2 = Checkbutton(tab2, text='Второй', variable=v2,background='#C7D2CC', font=("Arial Bold", 10), fg="#2B3B60")
    chk2.grid(column=1, row=0)
    chk3 = Checkbutton(tab2, text='Третий', variable=v3, background='#C7D2CC', font=("Arial Bold", 10), fg="#2B3B60")
    chk3.grid(column=2, row=0)

    bt = Button(tab2, text='Показать выбор', command=vibor, background='#C7D2CC', font=("Arial Bold", 10), fg="#2B3B60")
    bt.grid(column=3, row=0)



def vibor():
    mas = []
    if v1.get():
        mas.append('Первый')
    if v2.get():
        mas.append('Второй')
    if v3.get():
        mas.append('Третий')

    if mas:
        messagebox.showinfo('Выбор', "Вы выбрали: " + ", ".join(mas) + ' вариант')
    else:
        messagebox.showinfo('Выбор', 'Ничего не выбрано')

def text_work():
    global tx
    tx = Text(tab3, wrap='word')
    tx.pack(expand=1, fill='both')


    menu = Menu(window)
    window.config(menu=menu)

    mmenu = Menu(menu, tearoff=0)
    mmenu.add_command(label='Загрузить текст',background='#4E66A5', font=("Arial Bold", 9), foreground="white", command=tekst )

    menu.add_cascade(label='Файл',menu=mmenu)

def tekst():
    global tx
    fi = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if fi:
        with open(fi, 'r') as file:
            content = file.read()
            tx.delete(1.0, END)
            tx.insert(END, content)


prog()
window.mainloop()