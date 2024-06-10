import tkinter
from tkinter.constants import END
import tkinter.messagebox
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    generated_password = ""
    for char in password_list:
        generated_password += char

    print(f"Your password is: {generated_password}")
    password_input.delete(0, END)
    password_input.insert(0,generated_password)

def click_generate():
   generate()





# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_password(username,password,website):
    with open("./passwords.txt","a") as passwords_txt:
        passwords_txt.write(f"{website}  |  {username}  |  {password} \n")

def add_click():
    
    password = password_input.get()
    email = email_input.get()
    website = website_input.get()
    if len(password) > 0 and len(email) > 0 and len(website) > 0:

        is_ok =messagebox.askokcancel(title="k",message=f"Are you okay with {password} for {website}")
        
        if is_ok:
            write_password(email,password,website)

        website_input.delete(0, END)
        
        password_input.delete(0, END)
    else:
        messagebox.showerror(title="error",message="Don't leave any fields empty")





# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(width=300, height=300, padx=20, pady=20)
window.title("Password Manager")
canvas = tkinter.Canvas(width=200, height=200)

image_path = "./logo.png"
image = tkinter.PhotoImage(file=image_path)
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:",width=15)
email_label = tkinter.Label(text="Email/Username:",width=15)
password_label = tkinter.Label(text="Password:",width=15)

generate_button = tkinter.Button(text="Generate Password",width=15,command=click_generate)
add_button = tkinter.Button(text="Add",width=35,command=add_click)

website_input = tkinter.Entry(width=35)
email_input = tkinter.Entry(width=35)
password_input = tkinter.Entry(width=25)

website_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)

password_label.grid(row=3,column=0)
generate_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)
website_input.grid(row=1, column = 1,columnspan=2)
website_input.focus()
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"soeradj.mahabiersing@gmail.com")
password_input.grid(row=3,column=1)


window.mainloop()