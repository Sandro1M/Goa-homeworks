from turtle import *


#we wont to paint a houce

#step 1: drow a sqiare
speed(15)
width(7)

color("purple")



forward(200)  

left(90)

forward(200)

left(90)

forward(200)  

left(90)

forward(200)

left(90)
#end of squeare

#drowing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200 ,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#trying windows
color("purple")
left(30)
forward(40)

penup()
goto(190, 180)
pendown()

color("black")

left(-90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(10, 180)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)







exitonclick( )