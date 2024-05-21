from tkinter import *
import csv

def create():
    file = open("Ages.csv", "w")
    file.close()


def addtofile():
    file = open("Ages.csv", "a")
    name = nameEntry.get()
    age = ageEntry.get()
    newrecord = name  + "," + age + "\n" 
    file.write(str(newrecord))
    file.close()
    nameEntry.delete(0, END)
    ageEntry.delete(0, END)
    nameEntry.focus()

window = Tk()
window.geometry("500x500")
window.title("Demography Program")
window.resizable(False, False)

nameLabel = Label(text= "Enter a name: ", font=20)
nameLabel.place(x=20, y=70)

nameEntry = Entry(text='', font=20)
nameEntry.place(x=150, y=70)
nameEntry["justify"] = "left"
nameEntry.focus()

ageLabel = Label(text= "Enter their age: ", font=20)
ageLabel.place(x=20, y=110)

ageEntry = Entry(text=0, font=20)
ageEntry.place(x=150, y=110)
ageEntry["justify"] = "left"

button1 = Button(text="Create new file", command= create)
button1.place(x=150, y= 30)

button2 = Button(text="Add to file", command= addtofile)
button2.place(x=210, y= 150)

window.mainloop()
