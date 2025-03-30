import tkinter as tk
from tkinter import messagebox
import math  # For advanced operations like square root

# Function to update the display when a button is clicked
def update_display(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + value)

# Function to perform the arithmetic operations
def calculate():
    try:
        # Get the expression from the display
        expression = entry_display.get()
        
        # Evaluate the expression safely using eval()
        result = eval(expression)
        
        # Display the result
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
        
        # Save the calculation to a file
        save_calculation(expression, result)
        
        # Add to the history of calculations
        history_listbox.insert(tk.END, f"{expression} = {result}")
        
    except Exception as e:
        messagebox.showerror("Input Error", f"Error: {e}")

# Function to save the calculation and result to a text file
def save_calculation(expression, result):
    with open("calculation_results.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

# Function to clear the display and history
def clear():
    entry_display.delete(0, tk.END)
    history_listbox.delete(0, tk.END)  # Clear the history as well

# Function to implement backspace (delete the last character from the display)
def backspace():
    current_text = entry_display.get()
    entry_display.delete(len(current_text)-1, tk.END)

# Creating the main window
root = tk.Tk()
root.title("CALCULATOR")  # Set the title to "CALCULATOR"

# Set a light background color for the whole window
root.config(bg='#f0f8ff')  # Light blue background for the window

# Label for the title "Calculator" above the entry display
title_label = tk.Label(root, text="Calculator", font=('Arial', 20, 'bold'), bg='#f0f8ff')
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a display entry to show the current input (numbers and operators)
entry_display = tk.Entry(root, width=25, font=('Arial', 16), borderwidth=2, relief="solid", justify='right', bg="#f0f0f0")
entry_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Define the button labels (numbers and operations)
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3)
]

# Define button colors
button_colors = {
    'numbers': {'bg': '#b3c7e6', 'fg': '#000000'},  # Light blue background for numbers
    'operators': {'bg': '#ffad99', 'fg': '#000000'},  # Light red background for operators
    'equals': {'bg': '#d4edda', 'fg': '#000000'},    # Light green for equals button
    'clear': {'bg': '#f8d7da', 'fg': '#000000'},     # Light red for clear
    'backspace': {'bg': '#fff3cd', 'fg': '#000000'}   # Light yellow for backspace
}

# Create number and operation buttons dynamically with color
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16), command=calculate, bg=button_colors['equals']['bg'], fg=button_colors['equals']['fg'])
    elif text in ['+', '-', '*', '/']:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16), command=lambda text=text: update_display(text), bg=button_colors['operators']['bg'], fg=button_colors['operators']['fg'])
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16), command=lambda text=text: update_display(text), bg=button_colors['numbers']['bg'], fg=button_colors['numbers']['fg'])
    button.grid(row=row, column=col, padx=5, pady=5)

# Button for backspace with custom color and the backspace symbol (⌫)
button_backspace = tk.Button(root, text="⌫", width=5, height=2, font=('Arial', 16), command=backspace, bg=button_colors['backspace']['bg'], fg=button_colors['backspace']['fg'])
button_backspace.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Button for clearing the display with custom color
button_clear = tk.Button(root, text="Clear", width=10, height=2, font=('Arial', 16), command=clear, bg=button_colors['clear']['bg'], fg=button_colors['clear']['fg'])
button_clear.grid(row=6, column=2, columnspan=2, padx=5, pady=5)

# Label to display the history of calculations
history_label = tk.Label(root, text="History:", font=('Arial', 12), bg='#f0f8ff')
history_label.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

# Listbox to display the history of calculations
history_listbox = tk.Listbox(root, width=30, height=5, selectmode=tk.SINGLE, font=('Arial', 12), bg="#f0f0f0")
history_listbox.grid(row=8, column=0, columnspan=4, padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()
