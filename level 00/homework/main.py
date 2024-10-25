from turtle import *
width(7)

speed(0)

# draw a house skeleton
color("blue")

forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
left(90)


# drawing a door

penup()
goto(130, 0)
pendown()
color("yellow")
begin_fill()
left(90)
forward(130)
right(90)
forward(50)
right(90)
forward(130)
end_fill()

# drawing a rigth window

penup()
goto(280, 220)
pendown()
color("green")
begin_fill()
right(90)
forward(60)
left(90)

forward(40)
left(90)
forward(60)
left(90)
forward(40)
end_fill()

# drawing a left window

penup()
goto(20 , 220)
pendown()

begin_fill()
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

# drawing a roof

penup()
goto(300, 300)
pendown()

begin_fill()
left(45)
forward(215)
left(90)
forward(215)
end_fill()




exitonclick()