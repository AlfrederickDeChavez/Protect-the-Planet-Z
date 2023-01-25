import turtle
import random

def next():
    import Lecture


#Create the main screen
wn = turtle.Screen()
wn.title("Get Started!")
wn.setup(800, 600)
wn.bgpic("PPZbg.gif")



wn.listen()
wn.onkeypress(next, "c")
wn.onkeypress(next, "C")



wn.mainloop()