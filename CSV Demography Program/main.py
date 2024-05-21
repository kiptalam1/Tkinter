from tkinter import *
import csv


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
    name_list.focus()

def readlist():
    name_list.delete(0, END)
    file = list(csv.reader(open("Ages.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END, data)
        x = x + 1


window = Tk()
window.geometry("500x500")
window.title("CSV Demography Program")
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

button1 = Button(text="Add to file", command= addtofile)
button1.place(x=150, y= 150)

button2 = Button(text="Read list", command= readlist)
button2.place(x=150, y= 190)

namelist_label = Label(text= "List of names: ", font=20)
namelist_label.place(x=20, y=230)

name_list = Listbox()
name_list.place(x=150, y=230, width=250)


window.mainloop()
