import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import datetime

tasks = []

def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks.append(task_name)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showerror("Error", "Please enter a task name.")

def update_task():
    task_name = task_entry.get()
    selected_task = task_listbox.get(task_listbox.curselection()[0])
    if task_name and selected_task in tasks:
        tasks[tasks.index(selected_task)] = task_name
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showerror("Error", "Please select a task and enter a new task name.")

def delete_task():
    selected_task = task_listbox.get(task_listbox.curselection()[0])
    if selected_task in tasks:
        tasks.remove(selected_task)
        update_task_list()
    else:
        messagebox.showerror("Error", "Please select a task to delete.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
def thank_task():
    pass

def close_program():
    with open("To-Do_List.txt", "a") as file:
        current_datetime = datetime.now().strftime('%d-%m-%Y')
        message_with_datetime = f"Your current date is: {current_datetime}"
        file.write(message_with_datetime)
        file.write("\n")
        count = 1
        for task in tasks:
            file.write(f"({count}) Your {count} Task for today is:\n")
            file.write(task + "\n")
            count += 1
    root.destroy()

root = tk.Tk()
root.title("To-Do_List")

task_frame = tk.Frame(root)
task_frame.pack(pady=30)


task_entry = tk.Entry(task_frame, width=30)
task_entry.grid(row=0, column=0, padx=(20, 0))

add_button = tk.Button(task_frame, text="Add Task", bg="pink", font="Georgia", command=add_task)
add_button.grid(row=0, column=1, padx=(10, 0))

update_button = tk.Button(task_frame, text="Update Task", bg="pink", font="Georgia", command=update_task)
update_button.grid(row=0, column=2, padx=(10, 0))

delete_button = tk.Button(task_frame, text="Delete Task", bg="pink", font="Georgia", command=delete_task)
delete_button.grid(row=0, column=3, padx=(10, 20))
 


task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=20)

update_task_list()

close_button = tk.Button(root, text="Close", bg="light blue", font="Georgia", command=close_program)
close_button.pack(pady=20)

thank_button = tk.Button(root, text="THANK YOU ! ", bg="pink", font="Georgia", command=thank_task)
thank_button .pack( padx=(30))

root.mainloop()