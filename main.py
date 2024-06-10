import tkinter
from tkinter.constants import END


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_password(username,password,website):
    with open("./passwords.txt","a") as passwords_txt:
        passwords_txt.write(f"{website}  |  {username}  |  {password} \n")

def add_click():
    write_password(email_input.get(),password_input.get(),website_input.get())
    website_input.delete(0, END)
    
    password_input.delete(0, END)





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

generate_button = tkinter.Button(text="Generate Password",width=15)
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