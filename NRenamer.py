import os
import re
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from colorama import init


init(autoreset=True)

def rename_in_file(file_path, old_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        new_content = re.sub(re.escape(old_word), new_word, content, flags=re.IGNORECASE)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return f"Файл '{file_path}' обновлен."
    except Exception as e:
        return f"Ошибка при обработке файла '{file_path}': {e}"

def rename_in_directory(directory, old_word, new_word):
    results = []
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.endswith(('.txt', '.json', '.yml', '.yaml', '.xml', '.html', '.js', '.css')):
                result = rename_in_file(file_path, old_word, new_word)
                results.append(result)
    return results

def start_rename():
    directory = dir_entry.get()
    old_word = old_word_entry.get()
    new_word = new_word_entry.get() 

    if not os.path.isdir(directory):
        messagebox.showerror("Ошибка", "Указанная директория не существует.")
        return

    results = rename_in_directory(directory, old_word, new_word)
    messagebox.showinfo("Результаты", "\n".join(results))

def select_directory():
    directory = filedialog.askdirectory()
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, directory)


root = tk.Tk()
root.title("© Ренеймер - Developed by Noiryyy.exe")
root.geometry("550x500")
root.configure(bg="#f0f0f0")


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Выбрать папку", command=select_directory)
file_menu.add_command(label="Начать замену", command=start_rename)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)


help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="О программе", command=lambda: messagebox.showinfo("О программе", "Ренеймер файлов v1.2\nПрограмма для замены слов в файлах.\nCоздатель: Noiryyy.exe | NeverStudio"))
menu_bar.add_cascade(label="Справка", menu=help_menu)


root.config(menu=menu_bar)


frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Путь к папке:", bg="#f0f0f0").grid(row=0, column=0, sticky=tk.W, pady=5)
dir_entry = ttk.Entry(frame, width=50)
dir_entry.grid(row=0, column=1, pady=5)

tk.Button(frame, text="Выбрать папку", command=select_directory).grid(row=0, column=2, padx=5)

tk.Label(frame, text="Слово для замены:", bg="#f0f0f0").grid(row=1, column=0, sticky=tk.W, pady=5)
old_word_entry = ttk.Entry(frame, width=50)
old_word_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Новое слово:", bg="#f0f0f0").grid(row=2, column=0, sticky=tk.W, pady=5)
new_word_entry = ttk.Entry(frame, width=50)
new_word_entry.grid(row=2, column=1, pady=5)

tk.Button(frame, text="Начать замену", command=start_rename).grid(row=3, column=1, pady=20)


root.mainloop()