from tkinter import *


# define method caculate for converter
def caculate():
    print("calculate")
    miles = float(input_miles.get())
    km = round(miles * 1.609, 3)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

# input of Miles
input_miles = Entry(width=20, font=("Arial", 10, "italic"))
input_miles.grid(column=2, row=1)

# Label
result_label = Label(text="Is equal to", font=("Arial", 10, "italic"))
result_label.grid(column=1, row=2)

miles_label = Label(text="Miles", font=("Arial", 10, "italic"))
miles_label.grid(column=3, row=1)

km_label = Label(text="Km", font=("Arial", 10, "italic"))
km_label.grid(column=3, row=2)

km_result_label = Label(text="0", font=("Arial", 10, "italic"))
km_result_label.grid(column=2, row=2)

# Button
button = Button(text="Calculate", command=caculate)
button.config(padx=10)
button.grid(column=2, row=3)
mainloop()
