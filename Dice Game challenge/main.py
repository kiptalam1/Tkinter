from tkinter import *
import random

def roll():
    num = random.randint(1,6)
    dice_output["text"] = num

window = Tk()
window.geometry("300x300")
window.title("Roll Dice")
window.resizable(False, False)

dice_button = Button(text="Roll the dice", font=20, command=roll)
dice_button.place(x= 95, y=20, width=120, height=20)
dice_button["bg"] = "grey"
dice_button["fg"] = "white"


dice_output= Message(text="")
dice_output.place(x= 100, y=50, width=100, height=20)


window.mainloop()
