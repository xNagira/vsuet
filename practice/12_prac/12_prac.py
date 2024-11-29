from tkinter import*
from tkinter import messagebox
import requests
import json

window = Tk()
window.title("Собираем информацию о репозитории")
window.geometry('400x80')
def nm_rep():
    rname = name.get()
    if not rname:
        messagebox.showerror("Ошибка", "Введите имя репозитория")
        return

    url = f"https://api.github.com/users/{rname}"
    response = requests.get(url)

    if response.status_code == 200:
        repdata = response.json()
        datsave = {
            'company': repdata.get('company'),
            'created_at': repdata.get('created_at'),
            'email': repdata.get('email'),
            'id': repdata.get('id'),
            'name': repdata.get('name'),
            'url': repdata.get('html_url')
        }

        with open('repos_info.json', 'w') as file:
            json.dump(datsave, file, indent=4)

        messagebox.showinfo("Успешно", "Информация о репозитории сохранена в файл 'repos_info.json'")
    else:
        messagebox.showerror("Ошибка", "Репозиторий не найден")


lbl = Label(window, text="Имя репозитория:")
lbl.pack()

name= Entry(window, width=60)
name.pack()

btn = Button(window, text="Получить информацию", command=nm_rep)
btn.pack()

window.mainloop()