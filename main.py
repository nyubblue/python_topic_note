import smtplib
import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day
print(f"{year}/{month}/{day}")

day_of_week = now.weekday()
print(day_of_week)

weekday = now.weekday()
print(weekday)
print(now)
print(smtplib.SMTP_PORT)
#my_email = "thanhbuynitu@gmail.com"
#passw = "yxjgezqowsjqvfcz"
#connection = smtplib.SMTP("smtp.gmail.com")
#connection.starttls()
#connection.login(user=my_email, password=passw)
#connection.sendmail(from_addr=my_email, to_addrs="buynlt159@gmail.com", msg="Sent from my IDE. Hehe")
#connection.close()