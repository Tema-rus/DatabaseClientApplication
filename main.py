import tkinter as tk

# Создаем окно
root = tk.Tk()

# Устанавливаем заголовок окна
root.title('Клиентское приложение БД')

# Устанавливаем иконку
root.iconbitmap('favicon.ico')

# Устанавливаем минимальные и максимальные размеры окна
root.minsize(500, 500)
root.maxsize(900, 900)

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычисляем координаты верхнего левого угла окна, чтобы окно было по центру
x = (screen_width - 500) // 2
y = (screen_height - 500) // 2

# Устанавливаем позицию окна
root.geometry(f'500x500+{x}+{y}')

# Создаём кнопки
registration_btn = tk.Button(text='Регистрация')
login_btn = tk.Button(text='Войти')
settings_btn = tk.Button(text='Настройка к БД')

# Размещаем кнопки
registration_btn.pack()
login_btn.pack()
settings_btn.pack()

# Отображаем окно
tk.mainloop()
