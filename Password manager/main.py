from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]

    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def generate_file():
    website_text = website_input.get()
    username_text = username_input.get()
    password_text = password_input.get()
    new_login_data = {website_text: {
        "username": username_text,
        "password": password_text,
    }}

    if len(website_text) == 0 or len(username_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please, enter all the information.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_login_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_login_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Find PASSWORD ------------------------------- #
def search_password():
    website = website_input.get()
    try:
        with open('data.json', mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found!")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No data for {website} exists!")


# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image_src = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_src)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

website_input = Entry(width=33)
website_input.grid(column=2, row=2)
website_input.focus()

search_btn = Button(text="Search", width=15, command=search_password)
search_btn.grid(column=3, row=2)

username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=3)

username_input = Entry(width=52)
username_input.grid(column=2, row=3, columnspan=2)
username_input.insert(0, "d.kopac@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_input = Entry(width=33)
password_input.grid(column=2, row=4)

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=44, command=generate_file)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()
