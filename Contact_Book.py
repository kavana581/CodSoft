import tkinter as tk
from tkinter import messagebox

# Initialize a list to store contacts (as a list of dictionaries)
contacts = []

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and phone number are required!")
        return

    # Add the contact to the list
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})

    # Clear the input fields
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

    update_contact_list()

# Function to update the contact list display
def update_contact_list(filtered_contacts=None):
    # Clear the listbox before inserting updated contacts
    listbox_contacts.delete(0, tk.END)
    
    # If no filtered contacts, use all contacts
    display_contacts = filtered_contacts if filtered_contacts else contacts

    if not display_contacts:
        listbox_contacts.insert(tk.END, "No contacts found.")
    
    for contact in display_contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for contacts
def search_contact():
    search_term = entry_search.get().lower()
    # Filter contacts based on search term (name or phone)
    filtered_contacts = [contact for contact in contacts if 
                         search_term in contact['name'].lower() or search_term in contact['phone']]
    update_contact_list(filtered_contacts)

# Function to delete a contact
def delete_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contacts.pop(index)  # Remove the contact from the list
        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to update a contact
def update_contact():
    selected_contact_index = listbox_contacts.curselection()
    if selected_contact_index:
        index = selected_contact_index[0]
        contact = contacts[index]

        # Set the fields with the selected contact's details for editing
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)

        entry_name.insert(0, contact['name'])
        entry_phone.insert(0, contact['phone'])
        entry_email.insert(0, contact['email'])
        entry_address.insert(0, contact['address'])

        # Remove the contact from the list after loading its details
        contacts.pop(index)

        update_contact_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.config(bg="#e0f7fa")

# Title label
label_title = tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), bg="#e0f7fa")
label_title.pack(pady=20)

# Input fields for adding a new contact
label_name = tk.Label(root, text="Name:", font=("Arial", 12), bg="#e0f7fa")
label_name.pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

label_phone = tk.Label(root, text="Phone:", font=("Arial", 12), bg="#e0f7fa")
label_phone.pack(pady=5)
entry_phone = tk.Entry(root, font=("Arial", 12))
entry_phone.pack(pady=5)

label_email = tk.Label(root, text="Email:", font=("Arial", 12), bg="#e0f7fa")
label_email.pack(pady=5)
entry_email = tk.Entry(root, font=("Arial", 12))
entry_email.pack(pady=5)

label_address = tk.Label(root, text="Address:", font=("Arial", 12), bg="#e0f7fa")
label_address.pack(pady=5)
entry_address = tk.Entry(root, font=("Arial", 12))
entry_address.pack(pady=5)

# Add Contact Button
button_add = tk.Button(root, text="Add Contact", font=("Arial", 12), bg="#66bb6a", fg="white", command=add_contact)
button_add.pack(pady=10)

# Search Section
label_search = tk.Label(root, text="Search (Name or Phone):", font=("Arial", 12), bg="#e0f7fa")
label_search.pack(pady=5)
entry_search = tk.Entry(root, font=("Arial", 12))
entry_search.pack(pady=5)

button_search = tk.Button(root, text="Search", font=("Arial", 12), bg="#ffa726", fg="white", command=search_contact)
button_search.pack(pady=10)

# Listbox to display the contact list
listbox_contacts = tk.Listbox(root, font=("Arial", 12), height=8, width=40, selectmode=tk.SINGLE)
listbox_contacts.pack(pady=10)

# Buttons to update or delete a contact
button_update = tk.Button(root, text="Update Contact", font=("Arial", 12), bg="#42a5f5", fg="white", command=update_contact)
button_update.pack(pady=5)

button_delete = tk.Button(root, text="Delete Contact", font=("Arial", 12), bg="#f44336", fg="white", command=delete_contact)
button_delete.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()
