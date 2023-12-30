# Miles to Km Calculator
from tkinter import *

window = Tk()
window.title("Miles to Km Calcultor")
window.minsize(height=200, width=300)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609344, 3)
    label4.config(text=km)


entry = Entry(width=10)
entry.grid(row=0, column=1)

label1 = Label(text="Miles", font=("Constantia", 16, "normal"))
label1.grid(row=0, column=2)

label2 = Label(text="Km", font=("Constantia", 16, "normal"))
label2.grid(row=1, column=2)

label3 = Label(text="is equal to", font=("Constantia", 16, "normal"))
label3.grid(row=1, column=0)

label4 = Label(text="0", font=("Arial", 16, "normal"))
label4.grid(row=1, column=1)

button = Button(text="calculate", font=("Constantia", 12, "normal"), command=miles_to_km)
button.grid(row=2, column=1)



window.mainloop()