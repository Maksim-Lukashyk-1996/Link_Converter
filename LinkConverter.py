# Импортировал библиотеки
from tkinter import *
from tkinter import messagebox
import pyperclip
import pyshorteners

# Создал окно с помощью: tkinter
root = Tk()
# Прописал название нашего окна
root.title('Link_Converter')
# Задал размер окна с помощью: geometry
root.geometry('600x400')
# Задал цвет фона, нашему окну
root["bg"] = '#778899'
# Задал текст внутри нашего окна.
# Задал ему шрифт: font, Размер, Фон и Цвет
Label(root, text='Welcome to the \nLink_Converter', font='Colibri 20 bold',
      bg='#778899', fg='#FFFFFF').pack(pady=5)
Label(root, text='Enter link:', font='Colibri 15 bold',
      bg='#778899', fg='#FFFFFF').pack(pady=5)

# Создал поле, где будет ссылка
link = Entry(root, width=40)
link.pack()

# Создал новый текст
Label(root, text='Shortened link', font='Colibri 15 bold',
      bg='#778899', fg='#FFFFFF').pack(pady=5)

# Создал переменную, в которой будем хранить ссылку
res = Entry(root, width=40)
res.pack()


# Создал две функции: с помощью первой копируется ссылка с помощью кнопки.
# С помощью второй будем её именно сокращать.
def copytoclipboard():
    url = res.get()
    pyperclip.copy(url)
def short():
    # Если всё хорошо и ссылка корректная, тогда произойдёт её сокращение.
    try:
        a = link.get()
        s = pyshorteners.Shortener().tinyurl.short(a)
        res.insert(0, s)
    # Если ссылка будет некорректной, то будет ошибка.
    except:
        messagebox.showerror('Link Shortening', 'Invalid URL')

# Создали две кнопки, кнопки-взаимодействуют с функциями-которые прописаны выше.
Button(root, text='Cut down', command=short, activebackground='#778899',
       bd=5,  font='Colibri 13 bold', fg='#00BFFF').pack(pady=10)
Button(root, text='Copy', command=copytoclipboard, activebackground='#778899',
       bd=5, font='Colibri 13 bold', fg='#00BFFF').pack(pady=5)
Label(root, text='It-Overone </>', font='Colibri 15 bold', bg='#778899', fg='#00FFFF',).pack(pady=35)

# Вывод всего того, что прописали.
root.mainloop()


