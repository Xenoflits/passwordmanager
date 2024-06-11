import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox
import random
import json
import os
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = ''.join(password_list)

    print(f"Your password is: {generated_password}")
    password_input.delete(0, END)
    password_input.insert(0, generated_password)

def click_generate():
    generate()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_password(email, password, website):
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    # Check if the file exists
    if os.path.exists("passwords.json"):
        # Open the file in read mode to load existing data
        with open("passwords.json", "r") as passwords_json:
            try:
                data = json.load(passwords_json)
            except json.JSONDecodeError:
                # Handle the case where the file is empty or corrupted
                data = {}
    else:
        # If the file does not exist, start with an empty dictionary
        data = {}
        
    # Update the existing data with the new entry
    data.update(new_data)
    
    # Write the updated data back to the file in write mode
    with open("passwords.json", "w") as passwords_json:
        json.dump(data, passwords_json, indent=4)
        messagebox.showinfo(title="succes",message=f"Succesfully saved password and copied to clipboard")
        pyperclip.copy(password)
def add_click():
    password = password_input.get()
    email = email_input.get()
    website = website_input.get()

    if len(password) > 0 and len(email) > 0 and len(website) > 0:
        write_password(email, password, website)
        website_input.delete(0, END)
        password_input.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Don't leave any fields empty")

# ----------------------------  Search  ------------------------------- #     

def search():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as data:
            data = json.load(data)
            website = website_input.get()
            try:
                print(data[website])
            except:
                messagebox.showerror(title="no password",message="No password for this site")
            else:
                messagebox.showinfo(title="your password",message=f"Your password is {data[website]["password"]}")
                pyperclip.copy(data[website]['password'])
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
image_path = "logo.png"  # Ensure this path is correct and the file exists
image = tk.PhotoImage(file=image_path)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:", width=15, anchor="w")
email_label = tk.Label(text="Email/Username:", width=15, anchor="w")
password_label = tk.Label(text="Password:", width=15, anchor="w")

# Entries
website_input = tk.Entry(width=35, justify="left")  # Adjusted width for better layout
email_input = tk.Entry(width=35, justify="left")    # Adjusted width for better layout
password_input = tk.Entry(width=21, justify="left") # Adjusted width for better layout

# Buttons
generate_button = tk.Button(text="Generate Password", width=15, command=click_generate)
add_button = tk.Button(text="Add", width=36, command=add_click) # Adjusted width for better layout
search_button = tk.Button(text="Search", width=15, command=search)

# Layout using grid
website_label.grid(row=1, column=0, pady=5)
website_input.grid(row=1, column=1, pady=5, sticky="ew")
search_button.grid(row=1, column=2, padx=5, pady=5)

email_label.grid(row=2, column=0, pady=5)
email_input.grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")
email_input.insert(0, "soeradj.mahabiersing@gmail.com")

password_label.grid(row=3, column=0, pady=5)
password_input.grid(row=3, column=1, pady=5, sticky="ew")
generate_button.grid(row=3, column=2, padx=5, pady=5)

add_button.grid(row=4, column=1, columnspan=2, pady=10)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
