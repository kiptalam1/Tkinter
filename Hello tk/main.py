from tkinter import *

def greet():
    name = name_entry.get()
    message = str(f"Hello {name}")
    name_output_box["bg"] = "black"
    name_output_box["fg"] = "white"
    name_output_box["text"] = message
    name_output_box ["relief"] = "raised"

window = Tk()
window.geometry("400x400")
window.title("Hello")
window.resizable(False, False)

name_label = Label(text="Enter your name", font=20)
name_label.place(x=140, y=25)

name_entry = Entry(text='', font=20)
name_entry.place(x= 100, y=60, width=200, height=30)
name_entry['justify'] = 'center'
name_entry.focus()

name_button = Button(text="Enter", font=20, command=greet)
name_button.place(x= 125, y=100, width=150, height=30)

name_output_box =  Message(text = '')
name_output_box.place(x= 75, y=150, width=250, height=60)
name_output_box["bg"] = "white"
name_output_box["fg"] = "black"
name_output_box ["relief"] = "raised"


window.mainloop()
