from tkinter import *

def add_on():
    num = num_entry.get()
    num = int(num)
    answer = num_output["text"]
    answer = int(answer)
    total = num + answer
    num_output["text"] = total
    num_output["bg"] = "black"
    num_output["fg"] = "white"
    add_button["bg"] = "white"
    add_button["fg"] = "red"
    

def reset():
    total = 0
    num_output["text"] = 0
    num_entry.delete(0, END)
    num_entry.focus()
    num_output["fg"] = "black"
    num_output["bg"] = "white"
    add_button["bg"] = "white"
    add_button["fg"] = "black"
    

num = 0
total = 0
window = Tk()
window.geometry("500x500")
window.title("Addition program")

num_label = Label(text="Enter a number:", font=20)
num_label.place(x=50, y=20)

num_entry = Entry(text = 0)
num_entry.place(x=200, y=21, width=250, height=25)

add_button = Button(text="Add", font=20, command= add_on)
add_button.place(x=200, y=61, width=100, height=25)
add_button["bg"] = "white"

reset_button = Button(text="Reset", font=20, command= reset)
reset_button.place(x=350, y=61, width=100, height=25)
reset_button["bg"] = "white"

num_output = Message(text=0)
num_output.place(x=200, y=120, width=200, height=50)

window.mainloop()
