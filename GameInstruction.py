from tkinter import*


# Importing required modules 
  
import tkinter as tk 
import tkinter.scrolledtext as st 

def quiz():
        import PvZlike
# Creating tkinter window 
win = tk.Tk() 
win.title("How to Play") 
win.geometry("500x600")
win.configure(bg="green")
# Title Label 
tk.Label(win,  text = "Game Instruction",  font = ("Times New Roman", 20),  background = 'green',  foreground = "white").grid(column = 0, row = 10) 

nbutton = Button(win, text=">>", command=quiz, width=5,height=1, bg="green", fg="white", font=("times", 16, "bold"))
nbutton.place(x=400, y=5)
  
# Creating scrolled text area 
text_area = st.ScrolledText(win, width = 44,  height = 25,  font = ("Times New Roman", 15)) 
  
text_area.grid(column = 0, pady = 20, padx = 20) 
  
# Inserting Text which is read only 
text_area.insert(tk.INSERT, 
"""


> Press SPACE BAR to fire.

> Press UP ARROW KEY to move up. 

>Press DOWN ARROW KEY to move down. 

>Press RIGHT ARROW KEY to move right. 

>Press LEFT ARROW KEY to move left.


""") 
  
# Making the text read only 
text_area.configure(state ='disabled') 
win.mainloop()