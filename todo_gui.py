import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    task_listbox.delete(0, tk.END)
    if len(tasks) == 0: 
        task_listbox.insert(tk.END, "Your To-Do list is empty. ✨")
    else:
        for task in tasks:
            task_listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        display_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task. ❌")

# Function to delete a task
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        removed_task = tasks.pop(task_index)
        display_tasks()
        messagebox.showinfo("Task Deleted", f"Task '{removed_task}' has been deleted. 🗑️")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete. ❌")

# Function to mark a task as completed
def complete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks[task_index] += " ✅"
        display_tasks()
        messagebox.showinfo("Task Completed", f"Task '{tasks[task_index]}' has been marked as completed. ✅")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete. ❌")

# Function to update a task
def update_task():
    try:
        task_index = task_listbox.curselection()[0]
        old_task = tasks[task_index]
        new_task = task_entry.get()
        if new_task != "":
            tasks[task_index] = new_task
            display_tasks()
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Updated", f"Task '{old_task}' has been updated to '{new_task}'. ✏️")
        else:
            messagebox.showwarning("Input Error", "Please enter a new task description. ❌")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update. ❌")

# Create the main window
root = tk.Tk()
root.title("📝 To-Do List ✨")
root.geometry("500x500")
root.config(bg="#f4f4f9")

# Inspirational thought label in one line
thought_label = tk.Label(root, text="Start today with one small task, and the future will thank you. 🌱", 
                         font=('Arial', 12, 'italic'), fg="#4CAF50", bg="#f4f4f9", wraplength=400)
thought_label.pack(pady=10)

# Task entry field with placeholder
task_entry = tk.Entry(root, width=40, font=('Arial', 14), relief="solid", bd=2, fg="#424242")
task_entry.pack(pady=20)

# Instructional label to motivate the user
instruction_label = tk.Label(root, text="Enter your task: 📝", font=('Arial', 14, 'bold'), fg="#4CAF50", bg="#f4f4f9")
instruction_label.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task 📝", command=add_task, width=20, height=2, bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'))
add_button.pack(pady=5)

# Task listbox with scrollbar
task_listbox = tk.Listbox(root, width=50, height=10, font=('Arial', 12), selectmode=tk.SINGLE, bg="#e6e6e6", bd=2, relief=tk.GROOVE)
task_listbox.pack(pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)

# Button to delete a task
delete_button = tk.Button(root, text="Delete Task 🗑️", command=delete_task, width=20, height=2, bg="#f44336", fg="white", font=('Arial', 12, 'bold'))
delete_button.pack(pady=5)

# Button to mark a task as complete
complete_button = tk.Button(root, text="Mark as Completed ✅", command=complete_task, width=20, height=2, bg="#2196F3", fg="white", font=('Arial', 12, 'bold'))
complete_button.pack(pady=5)

# Button to update a task
update_button = tk.Button(root, text="Update Task ✏️", command=update_task, width=20, height=2, bg="#FF9800", fg="white", font=('Arial', 12, 'bold'))
update_button.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()
