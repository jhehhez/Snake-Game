from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game 1.0")
screen.tracer(0)
segments = []
position = [(20,0), (0,0), (-20,0)]

for x in range(3):
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position[x])
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    time.sleep(1)
    screen.update()
    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment - 1].xcor()
        new_y = segments[segment - 1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)



screen.exitonclick()