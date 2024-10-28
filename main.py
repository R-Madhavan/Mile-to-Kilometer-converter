from tkinter import *

def button_clicked():
    my_label1.config(text=round(int(input.get()) * 1.609))

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=20)

#labels
my_label1 = Label(text="0", font=("Arial", 10, "bold"))
my_label1["text"] = "0"
my_label1.grid(column=1,row=1)
my_label1.config(padx=10,pady=20)

my_label2 = Label(text="is equal to", font=("Arial", 10, ))
my_label2.grid(column=0,row=1)

my_label3 = Label(text="Miles", font=("Arial", 10, ))
my_label3.grid(column=2,row=0)

my_label4 = Label(text="Km", font=("Arial", 10, ))
my_label4.grid(column=2,row=1)

#Button
button1 = Button(text="Calculate", command=button_clicked)
button1.grid(column=1,row=2)

#Entry (component)
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1,row=0)

window.mainloop()
