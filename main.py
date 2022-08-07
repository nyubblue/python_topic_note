import fileinput
import re
from random import shuffle, randint, choice
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import pyperclip

# get line number of existed account
def getExistedLine(website, passwd, username):
    with open("passwd_manager.txt") as file:
        count = 0
        for line in file:
            wtemp = line.split("|")[0]
            utemp = line.split("|")[1]
            if wtemp == website and utemp == username:
                line = line.strip()
                file.close()
                return count
            count += 1
    file.close()
    return -1

# process for replacing the existed account
def replaceLine(line_number, data_line):
    with open("passwd_manager.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    data[line_number] = data_line
    print(data)

    with open('passwd_manager.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)


# callback when onChange input
def callback(iput):
    pattern = re.compile("(\\w)|@|[.]")
    if pattern.match(iput):
        print(iput)
        return True

    else:
        print(iput)
        print("SOS")
        return False


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, E)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    # Copy password to clipboard for something
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    passwd = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                              f"\nPassword: {passwd} \nIs it ok to save?")
        if is_ok:
            replacement = ""
            with open("passwd_manager.txt", "a") as file:
                print(f"{website}|{username}|{passwd}")
                exists_line_number = getExistedLine(website, passwd, username)
                if exists_line_number != -1:
                    file.close()
                    replaceLine(exists_line_number, f"{website}|{username}|{passwd}\n")
                    #replacement.replace(f"{website}|{username}|{passwd}\n", lines)
                    #fout.write(replacement)
                    #fout.close()
                else:
                    file.write(f"{website}|{username}|{passwd}\n")
                    file.close()
                #file.write(f"{website}|{username}|{passwd}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, sticky=W, columnspan=2)

# Label
website_label = Label(text="Website", font=("Arial", 10))
website_label.grid(row=1, column=0, sticky=E)
username_label = Label(text="Email/UserName", font=("Arial", 10))
username_label.grid(row=2, column=0, sticky=E)
password_label = Label(text="Password", font=("Arial", 10))
password_label.grid(row=3, column=0, sticky=E)

# Input
website_input = Entry(width=35)
website_input.grid(row=1, column=1, sticky=W, columnspan=2, pady=1)
username_input = Entry(master=window, width=35)
username_input.grid(row=2, column=1, sticky=W, columnspan=2, pady=1)
username_input.insert(0, "angela@gmail.com")
reg = window.register(callback)
username_input.config(validate="key", validatecommand=(reg, '%S'))

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=W, columnspan=1, pady=1)

# Buttons
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=W, columnspan=1, pady=1)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W, pady=1)

window.mainloop()
