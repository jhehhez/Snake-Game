from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()

screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game 1.0")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 19:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detect collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        game_is_on = False
        scoreboard.game_over()

    elif snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 19:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()