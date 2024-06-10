import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox
import random

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
def write_password(username, password, website):
    with open("passwords.txt", "a") as passwords_txt:
        passwords_txt.write(f"{website} | {username} | {password}\n")

def add_click():
    password = password_input.get()
    email = email_input.get()
    website = website_input.get()

    if len(password) > 0 and len(email) > 0 and len(website) > 0:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Are you okay with using '{password}' for '{website}'?")
        if is_ok:
            write_password(email, password, website)
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Don't leave any fields empty")

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
website_label = tk.Label(text="Website:", width=15)
email_label = tk.Label(text="Email/Username:", width=15)
password_label = tk.Label(text="Password:", width=15)

# Buttons
generate_button = tk.Button(text="Generate Password", command=click_generate)
add_button = tk.Button(text="Add", width=35, command=add_click)

# Entries
website_input = tk.Entry(width=35)
email_input = tk.Entry(width=35)
password_input = tk.Entry(width=25)

# Layout
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "soeradj.mahabiersing@gmail.com")

password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1)
generate_button.grid(row=3, column=2)

add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
