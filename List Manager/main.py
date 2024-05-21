from tkinter import *
#define the functions
namelist = []
def addtolist():
    name = nameEntry.get()
    namelist.append(name)
    nameoutput['text'] = namelist

def clearlist():
    namelist = []
    nameoutput['text'] = ''
    nameEntry.delete(0, END)
    nameEntry.focus()
    



window = Tk()
window.geometry('400x400')
window.title("List manager")
window.resizable(False, False)

nameLabel = Label(text='Enter a Name: ', font=20)
nameLabel.place(x=20, y=30)

nameEntry = Entry(text= '', font=20)
nameEntry.place(x=130, y=30)

addButton = Button(text= 'Add', font=20, command= addtolist)
addButton.place(x=130, y=60, width=60)

deleteButton = Button(text= 'Clear', font=20, command= clearlist)
deleteButton.place(x=253, y=60, width=60)

nameoutput = Message(text='', font=20)
nameoutput.place(x=75, y=90, width=400, height=400)

window.mainloop()
