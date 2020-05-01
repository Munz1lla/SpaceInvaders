#Space Invaders - part 1
#Set up the screen
#Python 
import turtle
import math
import random
import winsound
import platform

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title ("Space Invaders")
wn.bgpic("~/Desktop/Python_projects/space_invaders_background.gif")
wn.tracer(0)

#register the shapes
wn.register_shape("~/Desktop/Python_projects/invader.gif")
wn.register_shape("~/Desktop/Python_projects/player.gif")


#Draw border
turtle.pen(fillcolor="white", pencolor="white", pensize=6)
turtle.penup()
turtle.setposition(-300, -300)
turtle.pendown()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)

#set the score to 0
score = 0
#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the Player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("~/Desktop/Python_projects/player.gif")
player.penup()
player.speed(0) #calling the method
player.setposition(0, -250)
player.setheading(90)
player.speed = 0 #calling the variable

#choose the number of enemies
number_of_enemies = 30
#create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

    enemy_start_x = -225
    enemy_start_y = 250
    enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("~/Desktop/Python_projects/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    #update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0
        
enemyspeed = 0.4


#create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 7

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player left and right
def move_left():
    player.speed = -3
    

def move_right():
    player.speed = 3
    

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:# This line stops the player from exceeding the boundaries of the border>LEFT
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("C:/Users/user/Desktop/Python_projects/laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        #move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#create keyboard binding
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")



#main game loop
while True:

    wn.update()
    move_player()

    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)


        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Moves all the enemies down at once
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change the enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change the enemy direction
            enemyspeed *= -1
        #check for a collision between the bullet andthe enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("C:/Users/user/Desktop/Python_projects/explosion.wav", winsound.SND_ASYNC)
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            enemy.setposition(0, 10000)
            #Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            

        if isCollision(player, enemy):
            winsound.PlaySound("C:/Users/user/Desktop/Python_projects/explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break


    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



