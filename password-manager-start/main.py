from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# json files don't allow duplicity

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # To generate passwords multiple times in the same instance
    password_output.delete(0, END)
    pass_list = [choice(letters) for i in range(0, randint(8, 10))] + [choice(numbers) for i in
                                                                       range(0, randint(2, 4))] + [choice(symbols) for i
                                                                                                   in range(0,
                                                                                                            randint(2,
                                                                                                                    4))]
    shuffle(pass_list)
    password_output.insert(0, ''.join(pass_list))
    pyperclip.copy(''.join(pass_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_details():
    website = website_input.get().title()
    user = user_input.get()
    password = password_output.get()

    if website != '' and user != '' and password != '':
        is_ok = messagebox.askokcancel(title=website, message='You have entered the following details:\n'
                                                                      f'User: {user}\nPassword: {password}\n'
                                                                      'Is it ok to save to data.json?')
        if is_ok:
            new_dict = {
                website: {
                    'email': user,
                    'password': password
                }
            }

            try:
                with open('data.json', mode='r') as file:
                    # Read old data
                    data = json.load(file)
                    # Update old data
                    data.update(new_dict)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    data = new_dict

            with open('data.json', mode='w') as file:
                # Write new data
                json.dump(data, file, indent=4)

            website_input.delete(0, END)
            password_output.delete(0, END)
            user_input.delete(0, END)
            user_input.insert(0, 'mallalikhitha9@gmail.com')
            website_input.focus()
    else:
        messagebox.showwarning(title='Oops', message='Please don\'t leave any field empty')


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_input.get().title()
    if website != '':
        try:
            with open('data.json') as file:
                data = json.load(file)
                email = data[website]['email']
                password = data[website]['password']
                is_yes = messagebox.askyesno(title=website, message='The details you saved last for this website is:\n'
                                                                    f'email: {email}\npassword: {password}\n'
                                                                    'Do you want to copy the password?')
                if is_yes:
                    pyperclip.copy(password)
        except KeyError:
            messagebox.showwarning(title='Oops', message='No Data Found.')
        except FileNotFoundError:
            messagebox.showwarning(title='Oops', message='No data.json file found.')
    else:
        messagebox.showwarning(title='Oops', message='There\'s nothing to search..')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

# Create Canvas
canvas = Canvas(window, height=200, width=200)
bg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', font=('Arial', 12))
website_label.grid(row=1, column=0)
user_label = Label(text='Email/Username:', font=('Arial', 12))
user_label.grid(row=2, column=0, pady=2.5)
password_label = Label(text='Password:', font=('Arial', 12))
password_label.grid(row=3, column=0)

# Entries
website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky='nesw')
user_input = Entry()
user_input.insert(0, 'mallalikhitha9@gmail.com')
user_input.grid(row=2, column=1, columnspan=2, sticky='nesw', pady=2.5)
password_output = Entry()
password_output.grid(row=3, column=1, sticky='nesw')

# Buttons
generate_pass_button = Button(text='Generate Password', command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky='nesw')
add_pass_button = Button(text='Add', command=add_details)
add_pass_button.grid(row=4, column=1, columnspan=2, sticky='nesw', pady=(2.5, 30))
search_button = Button(text='Search', command=search)
search_button.grid(row=1, column=2, sticky='nesw')

window.mainloop()
