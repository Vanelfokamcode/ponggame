import turtle

wn = turtle.Screen()
wn.title ("Pong by Vanelfokam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score 
score_a = 0
score_b = 0
#PaddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set the fastest speed animation possible
paddle_a.shape("square") #la forme su paddle_a
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #by default the shape is 20pix so we resize it 
paddle_a.penup() #not drawing while moving
paddle_a.goto(-350, 0) #left = -350 middle = 0 right = 350

#PaddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0) #set the fastest speed animation possible
paddle_b.shape("square") #la forme su paddle_a
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #by default the shape is 20pix so we resize it 
paddle_b.penup() #not drawing while moving
paddle_b.goto(350, 0) #left = -350 middle = 0 right = 350

#Ball 
ball = turtle.Turtle()
ball.speed(0) #set the fastest speed animation possible
ball.shape("square") #la forme su paddle_a
ball.color("white")
ball.penup() #not drawing while moving
ball.goto(0, 0) #left = -350 middle = 0 right = 350
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up(): #take the y coordinate and add 20 to that to go up 
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down(): #take the y coordinate and soubstract 20 to that to go down 
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up(): #take the y coordinate and add 20 to that to go up 
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down(): #take the y coordinate and soubstract 20 to that to go down 
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#Keybord input
wn.listen() #tell the programm to listen to the keyword input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "h")
wn.onkeypress(paddle_b_down, "b")

#Main game loop

 
while True: 
     wn.update()

     #Move the ball
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() + ball.dy)

     # Border check

     if ball.ycor() > 290: #if the y coordinate is greater than the height from the middle to 
         # the bottom which is 300 minus 10 the white bar 
         ball.sety(290)
         ball.dy *= -1 #change the direction of the ball

     if ball.ycor() < -290: #if the y coordinate is greater than the height from the middle to 
         # the bottom which is 300 minus 10 the white bar 
         ball.sety(-290)
         ball.dy *= -1 #change the direction of the ball

     if ball.xcor() > 350:
         score_a += 1
         pen.clear()
         pen.write("Player A: {}  Player B: {}".format(score_a, score_b))
         ball.goto(0,0)
         ball.dx *= -1

     if ball.xcor() < -390:
         ball.goto(0,0)
         ball.dx *= -1

     #paddle and ball collisions
     if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
         ball.setx(340)
         ball.dx *= -1

     if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
         ball.setx(-340)
         ball.dx *= -1
