import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # We need to install pyperclip for copying to clipboard

# Function to generate a random password
def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool and join them into a password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the password generation
def on_generate():
    try:
        # Get the password length from the input box
        length = int(entry_length.get())
        
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password in the result label
        label_result.config(text=f"Generated Password: {password}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")

# Function to copy the generated password to clipboard
def copy_to_clipboard():
    password = label_result.cget("text").replace("Generated Password: ", "")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password generated to copy.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")  # Adjusting the size to make it a little larger
root.config(bg="#f0f8ff")  # Set background color

# Label for the title
label_title = tk.Label(root, text="Password Generator", font=('Arial', 18, 'bold'), bg="#f0f8ff", fg="#333")
label_title.pack(pady=20)

# Label for password length
label_length = tk.Label(root, text="Enter password length (>=6):", font=('Arial', 12), bg="#f0f8ff", fg="#333")
label_length.pack(pady=10)

# Entry box to input the password length
entry_length = tk.Entry(root, font=('Arial', 14), width=20, justify='center', bd=2, relief="solid")
entry_length.pack(pady=10)

# Button to generate the password
button_generate = tk.Button(root, text="Generate Password", font=('Arial', 14, 'bold'), command=on_generate, bg="#4CAF50", fg="white", relief="raised", width=20)
button_generate.pack(pady=20)

# Label to display the generated password
label_result = tk.Label(root, text="Generated Password: ", font=('Arial', 12), bg="#f0f8ff", wraplength=350, fg="#555")
label_result.pack(pady=10)

# Button to copy the password to clipboard
button_copy = tk.Button(root, text="Copy to Clipboard", font=('Arial', 12), command=copy_to_clipboard, bg="#FFD700", fg="black", relief="raised", width=20)
button_copy.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
