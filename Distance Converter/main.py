from tkinter import *

def kmtomiles():
    km_distance = distanceEntry.get()
    km_distance = float(km_distance)
    miles = km_distance * 0.6214 
    answer = "%.4f" % miles
    answerBox['text'] = f"{str(answer)} miles"
    distanceEntry.delete(0, END)
    
def milestokm():
    m_distance = distanceEntry.get()
    m_distance = float(m_distance)
    km = m_distance * 1.6093
    answer = "%.4f" % km
    answerBox["text"] = f"{str(answer)} kilometers"
    distanceEntry.delete(0, END)


window = Tk()
window.geometry("500x500")
window.title("Distance Converter")
window.resizable(False, False)

distanceLabel = Label(text="Enter distance: ", font=20)
distanceLabel.place(x=20, y=25)

distanceEntry = Entry(text=0, font=20)
distanceEntry.place(x= 150, y= 25, width=300)

convertLabel = Label(text="Convert from: ", font= 20)
convertLabel.place(x=20, y=80)

kmButton = Button(text="Kms to Miles", font=20, command = kmtomiles)
kmButton.place(x=160, y=70)

milesButton = Button(text="Miles to Kms", font=20, command= milestokm)
milesButton.place(x=340, y=70)

answerBox = Message(text=0, font=25)
answerBox.place(x=150, y=140, width=250, height=50)

window.mainloop()
