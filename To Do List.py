import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")

# Widgets
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=30, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=50)
task_listbox.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=30, command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
