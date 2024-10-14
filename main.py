BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd 
from tkinter import *
import random
current = {}
learning = {}
try:
    data =  pd.read_csv("projects/capstone/learn_words.csv")
except:
    main = pd.read_csv("projects/capstone/french_words.csv")
    learning = main.to_dict(orient="records")
else:
    learning = data.to_dict(orient="records")


def next():
    global current,timer
    window.after_cancel(timer)
    current = random.choice(learning)
    canva.itemconfig(title,text="French",fill="red")
    canva.itemconfig(word,text=current["French"],fill="red")
    canva.itemconfig(img,image = pic)
    timer = window.after(5000, func=eng)
    

def eng():
    canva.itemconfig(title,text="English",fill="green")
    canva.itemconfig(word,text=current["English"],fill="green")
    canva.itemconfig(img,image = pic1)

def learn():
    learning.remove(current)
    data = pd.DataFrame(learning)
    data.to_csv("projects/capstone/learn_words.csv",index=FALSE)
    next()


window = Tk()
window.title("Meaning Card")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
timer = window.after(5000, func=eng)







canva = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
pic = PhotoImage(file="projects/capstone/card_front.png")
pic1 = PhotoImage(file="projects/capstone/card_back.png")
right = PhotoImage(file="projects/capstone/right.png")
wrong = PhotoImage(file="projects/capstone/wrong.png")
img = canva.create_image(400,275,image = pic)
title = canva.create_text(400,150, text = "TITLE", font=("Courier",50,"bold"))
word = canva.create_text(400,270, text = "WORD", font=("Courier",80,"bold"))
canva.grid(row=0,column=0,columnspan=2)

cross = Button(image=wrong,highlightthickness=0,command=next)
cross.grid(row=1,column=0)
tick = Button(image=right,highlightthickness=0,command=learn)
tick.grid(row=1,column=1)






next()



window.mainloop()