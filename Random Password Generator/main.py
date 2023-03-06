PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
import pyperclip


def generate_password():
    '''

    :return:
    '''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for letter in range(nr_letters)]

    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import *
from tkinter import messagebox
import json


def save_password():
    '''

    :return:
    '''
    email = email_input.get()
    password = password_input.get()
    website = website_input.get()
    new_data = {website:
        {
            "email": email,
            "password": password,
        }
    }
    if len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please provide correct password")
    elif len(website) == 0:
        messagebox.showinfo(title="Warning", message="Please provide correct website")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("text.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("text.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("text.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)


def search():
    try:
        with open("text.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        website = website_input.get()
        messagebox.askokcancel(title=website, message=f"Error no data file")
    else:
        website = website_input.get()
        if website in data:
            print(website)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \nEmail: {email} \nPassword: {password}")
        else:
            messagebox.askokcancel(title=website, message=f"No data for {website}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)

# Column 0

website = Label(text="Website: ", fg=GREEN, font=(FONT_NAME, 16, "bold"))
website.grid(column=0, row=1)

email = Label(text="Email/Username: ", fg=GREEN, font=(FONT_NAME, 16, "bold"))
email.grid(column=0, row=2)

password = Label(text="Password: ", fg=GREEN, font=(FONT_NAME, 16, "bold"))
password.grid(column=0, row=3)

# Column 1

website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

website_search = Button(text="Search", width=14, highlightthickness=0, command=search)
website_search.grid(column=2, row=1)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "mbajdel@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

button_1 = Button(text="Generate Password", highlightthickness=0, command=generate_password)
button_1.grid(column=2, row=3)

add = Button(text="Add", width=43, highlightthickness=0, command=save_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
