import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectbackground="lightblue", selectmode=tk.SINGLE, bg="#f0f0f0")
listbox.pack(pady=10)

# Create an entry field for adding tasks
entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=10)

# Create buttons for adding and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#FF5733", fg="white")

add_button.pack(pady=5)
remove_button.pack()

# Run the GUI application
root.mainloop()
