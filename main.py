import random
import smtplib
from datetime import datetime
from tkinter import *
from tkcalendar import DateEntry
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)


# function
def send_submit():
    data = pandas.read_csv("birthdays_copy.csv")
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
    if today_tuple in birthdays_dict:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            my_email = "thanhbuynitu@gmail.com"
            passw = "yxjgezqowsjqvfcz"
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=passw)
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            with open(file_path) as letter_file:
                birthday_person = birthdays_dict[today_tuple]
                contents = letter_file.read()
                contents = contents.replace("[NAME]", birthday_person["name"])
            connection.sendmail(from_addr=my_email, to_addrs={birthday_person["email"]}
                                , msg=f"Subject:Happy Birthday!\n\n{contents}")
            connection.close()
            print("SUCCESS")


def add_submit():
    data = pandas.read_csv("birthdays_copy.csv")
    data_dict = data.to_dict()
    headers = [key for (key, value) in data.items()]
    date = datetime.fromisoformat(str(cal.get_date()))
    day = date.day
    month = date.month
    year = date.year
    columns = ["Buyn", email_input.get(), str(year), str(month), str(day)]
    df_new = {header: columns[idx] for (idx, header) in enumerate(headers, start=0)}

    idx = 0
    for (key, value) in data_dict.items():
        maxIdx = len(value.items())
        value[maxIdx] = columns[idx]
        idx += 1
    df = pandas.DataFrame.from_dict(data_dict)
    df.to_csv("birthdays_copy.csv", index=False, header=True)


window = Tk()
window.title("BirthDay App")
window.minsize(width=600, height=500)
window.config(padx=50, pady=50, background="#D6F6F4")

# label
header_lbl = Label(text="App", font=("Arial", 30, "bold"), background="#D6F6F4")
header_lbl.grid(row=0, column=0, columnspan=2, sticky=S)
email_lbl = Label(text="Email", font=("Arial", 15, "bold"), background="#D6F6F4")
email_lbl.config(padx=10, pady=10)
email_lbl.grid(column=0, row=1)
birth_lbl = Label(text="Birth Day", font=("Arial", 15, "bold"), background="#D6F6F4")
birth_lbl.config(padx=10, pady=10)
birth_lbl.grid(row=2, column=0)

# Input
email_input = Entry(width=35, font=("Arial", 15, "italic"))
email_input.grid(column=1, row=1)
cal = DateEntry(window, selectmode="day", font=("Arial", 15), date_pattern="yyyy-MM-dd", date_format="yyyy-MM-dd")
cal.grid(row=2, column=1)

# Button
add_button = Button(width=30, background="#27A1B0", text="Add Email", highlightthickness=0)
add_button.config(font=("Arial", 15, "bold"), fg="white", command=add_submit)
add_button.grid(column=1, row=4, columnspan=2)
#
submit_button = Button(width=30, background="#27A1B0", text="Send", highlightthickness=0)
submit_button.config(font=("Arial", 15, "bold"), fg="white", command=send_submit)
submit_button.grid(column=1, row=5, columnspan=2)

mainloop()

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
