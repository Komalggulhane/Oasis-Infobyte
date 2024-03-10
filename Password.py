import tkinter as tk
from tkinter import messagebox
import random
import string

def get_user_input():
    if gui_mode.get() == 1: # Check if GUI mode is enabled
        try:
            length = int(length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
            return None, None

        character_types = character_types_var.get()

        character_sets = []
        if 'letters' in character_types:
            character_sets.append(string.ascii_letters)
        if 'numbers' in character_types:
            character_sets.append(string.digits)
        if 'symbols' in character_types:
            character_sets.append(string.punctuation)

        if not character_sets:
            messagebox.showerror("Error", "At least one character type must be selected.")
            return None, None

        return length, character_sets
    else: # Command-line mode
        while True:
            try:
                length = int(input("Enter password length: "))
                if length < 1:
                    print("Password length must be at least 1.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            character_types = input("Enter character types (letters, numbers, symbols): ").lower()
            if not character_types:
                print("At least one character type must be selected.")
                continue

            character_sets = []
            if 'letters' in character_types:
                character_sets.append(string.ascii_letters)
            if 'numbers' in character_types:
                character_sets.append(string.digits)
            if 'symbols' in character_types:
                character_sets.append(string.punctuation)

            if not character_sets:
                print("At least one character type must be selected.")
                continue

            return length, character_sets

def generate_password(length, character_sets):
    password = ''
    for _ in range(length):
        character_set = random.choice(character_sets)
        password += random.choice(character_set)

    return password

def display_password(password):
    if gui_mode.get() == 1: # Check if GUI mode is enabled
        password_label.config(text=password)
    else: # Command-line mode
        print("Generated password:", password)

def generate_and_display():
    try:
        length, character_sets = get_user_input()
        if length is not None and character_sets is not None:
            password = generate_password(length, character_sets)
            display_password(password)
    except ValueError as e:
        if gui_mode.get() == 1: # Check if GUI mode is enabled
            messagebox.showerror("Error", str(e))
        else: # Command-line mode
            print("Error:", e)

app = tk.Tk()
app.title("Password Generator")

length_label = tk.Label(app, text="Password length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1)

character_types_var = tk.StringVar()
character_types_checkboxes = []

for i, character_type in enumerate(['letters', 'numbers', 'symbols']):
    checkbox = tk.Checkbutton(app, text=character_type, variable=character_types_var, onvalue=character_type, offvalue='')
    checkbox.grid(row=1, column=i)
    character_types_checkboxes.append(checkbox)

generate_button = tk.Button(app, text="Generate", command=generate_and_display)
generate_button.grid(row=2, column=0, columnspan=3)

password_label = tk.Label(app, text="")
password_label.grid(row=3, column=0, columnspan=3)

gui_mode = tk.IntVar() # Variable to track GUI mode
checkbox = tk.Checkbutton(app, text="Enable GUI Mode", variable=gui_mode)
checkbox.grid(row=4, column=0, columnspan=3)

app.mainloop()

