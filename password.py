import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    # Get user input for password length
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return
    
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return
    
    # Get user input for character types
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    if not (use_letters or use_numbers or use_symbols):
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_chars = letters + numbers + symbols
    
    if len(all_chars) == 0:
        messagebox.showerror("Error", "No character types selected.")
        return
    
    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    password_label.config(text=f"Generated Password: {password}")


# Create the main window
window = tk.Tk()
window.geometry("400x300")
window.title("Random Password Generator")

length = tk.Label(window, text="Enter password length:")
length.pack()
length_entry = tk.Entry(window)
length_entry.pack(pady=(20,0))


letters_var = tk.BooleanVar()
letters_check = tk.Checkbutton(window, text="Letters", variable=letters_var)
letters_check.pack(pady=(20,0))

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
numbers_check.pack()

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Symbols", variable=symbols_var)
symbols_check.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=(20,0))

password_label = tk.Label(window, text="")
password_label.pack(pady=(30,0))


window.mainloop()
