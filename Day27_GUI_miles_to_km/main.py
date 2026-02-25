from tkinter import *
def calculate():
    miles = float(entry.get())
    km = miles * 1.0934
    label3.config(text=km)

window = Tk()
window.title("Miles to Km converter")
window.config(padx = 70, pady= 20)

#Textbox
entry = Entry(width= 7 )
entry.insert(END, "0")
entry.grid(row=0, column=1)


#Label
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

km = 0
label3 = Label(text=km)
label3.grid(row=1, column=1)

label4 = Label(text="km")
label4.grid(row=1, column=2)

button = Button(text="calculate", command= calculate)
button.grid(row=2, column=1)

window.mainloop()
