from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

# Lable

my_level = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_level.config(text="New Text")
my_level.grid(column=0, row=0)
my_level.config(padx=50, pady=50)


# Button

def button_clicked():
    new_text = input.get()
    print("I Got Clicked.")
    my_level.config(text=new_text)


button = Button(text="click me ", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=2, row=2)


window.mainloop()
