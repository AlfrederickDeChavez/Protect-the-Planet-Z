import turtle
import random


#Create the screen

wn = turtle.Screen()
wn.title("Protect the Planet Z")
wn.setup(800, 600)
#wn.bgcolor("black")
wn.bgpic("mybg.gif")
wn.tracer(0)

wn.register_shape("dont.gif")
wn.register_shape("saw.gif")
wn.register_shape("bulb.gif")
wn.register_shape("storm.gif")
wn.register_shape("plant.gif")



pen = turtle.Turtle()
pen.speed(0)
pen.penup()

#Create the classes
#class Player(turtle.Turtle):
class Player():
    def __init__(self):
        #turtle.Turtle.__init__(self)
        self.color = "red"
        #self.penup()
        self.x = -350
        self.y = 0
        #self.goto(-350, random.randint(-290, 290))
        self.shape = "bulb.gif"
        #self.speed(0)
        self.dy = 0
        self.dx = 0

    def up(self):
        self.dy = 1
        self.dx = 0
    
    def down(self):
        self.dy = -1
        self.dx = 0

    def left(self):
        self.dx = -1
        self.dy = 0
    
    def right(self):
        self.dx = 1
        self.dy = 0

    def move(self):
        #self.sety(self.ycor() + self.dy)
        self.y = self.y + self.dy
        self.x = self.x + self.dx

        #Check for border collision
        if self.y > 280:
            self.y = 280
            self.dy = 0

        elif self.y < -280:
            self.y = -280
            self.dy = 0
        
        if self.x < -390:
            self.x = -390
            self.dx = 0

        if self.x < -290:
            self.x = -290
            self.dx = 0

        
    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y -  other.y) ** 2) ** 0.5
        return d

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(1, 1, 0)
        pen.color(self.color)
        pen.stamp()   

#class Missile(turtle.Turtle):
class Missile():

    def __init__(self):
        self.color = "black"
        #self.penup()
        self.x = -450
        self.y = 0
        self.shape = "dont.gif"
        self.size = random.randint(1, 9) / -10
        self.dx = 0

    def fire(self):
        self.x = player.x 
        self.y = player.y 
        self.dx = 2

    def move(self):
        self.x = self.x + self.dx

    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y -  other.y) ** 2) ** 0.5
        return d

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.4, 0.4, 0)
        pen.color(self.color)
        pen.stamp()   

class Enemy():
    def __init__(self):
        shapes = ["saw.gif", "storm.gif"]
        colors = ["blue", "black", "purple", "pink", "gray"]
        self.color = random.choice(colors)
        #self.penup()
        self.x = 380
        self.y = random.randint (-250, 250)
        self.shape = random.choice(shapes)
        self.dx = -0.1
        
    def move(self): 
        self.x = self.x + self.dx
            #Border Check
        if self.x < -400:
            self.x = 400
            self.y = random.randint(-250, 250)
            self.dx *= 1.1


        


    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y -  other.y) ** 2) ** 0.5
        return d

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(1, 1, 0)
        pen.color(self.color)
        pen.stamp()   


class Shield():
    def __init__(self):
        self.color = "green"
        self.x = -380
        self.y = random.randint(-250, 250)
        self.shape = "plant.gif"


    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y -  other.y) ** 2) ** 0.5
        return d

        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(1, 1, 0)
        pen.color(self.color)
        pen.stamp() 


score = 0

#Display the score
pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.speed(0)
pen1.shape("circle")
pen1.color("white")
pen1.penup()
pen1.goto(-350, 260)
font = ("Times New Roman", 20, "normal")
pen1.write("Score: {}".format(score), align="center", font=font)


#Create game objects

player = Player()
missile = Missile()
shield = Shield()

#Create a list
enemies = []
noofe = 15
for _ in range(noofe):
    enemies.append(Enemy())

shields = []
for _ in range(15):
    shields.append(Shield())



#Keyboard Bindings

wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")
wn.onkeypress(missile.fire, "space")






while True:

    wn.update()
    pen.clear()

    player.move()
    missile.move()
    player.render(pen)
    missile.render(pen)



    for enemy in enemies:
        enemy.move()



        #Check for collsion
        if enemy.distance(missile) < 13:
            enemy.x = 1000000
            enemy.y = random.randint(-250, 250)
            missile.dx = 0
            missile.x = 0
            missile.y = 1000
            score +=1
            pen1.clear()
            pen1.write("Score: {}".format(score), align="center", font=font)


        if enemy.x < -350:
            pen2 = turtle.Turtle()
            pen2.hideturtle()
            pen2.speed(0)
            pen2.shape("circle")
            pen2.color("red")
            pen2.penup()
            pen2.goto(0, 0)
            font = ("Times New Roman", 20, "normal")
            pen2.write("PLANET Z HAS BEEN DESTROYED!", align="center", font=font)   

        if score == 15:
            pen3 = turtle.Turtle()
            pen3.hideturtle()
            pen3.speed(0)
            pen3.shape("circle")
            pen3.color("red")
            pen3.penup()
            pen3.goto(0, 0)
            font = ("Times New Roman", 20, "normal")
            pen3.write("YOU SAVED THE PLANET!", align="center", font=font) 

        enemy.render(pen)
        
    for shield in shields:
        shield.render(pen)
        if enemy.distance(shield) < 13:
            enemy.x = 1000000
            enemy.y = random.randint(-250, 250)
            shield.x = 1000000
            shield.y = 1000000
            score +=1
            pen1.clear()
            pen1.write("Score: {}".format(score), align="center", font=font)





