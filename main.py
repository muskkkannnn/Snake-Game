from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# starting_positions = [(0,0), (-20,0), (-40,0)]                     //Previous Code without OOP

# segments = []

# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()

#     new_segment.goto(position)
#     segments.append(new_segment)

# print(segments)

#Controlling Snake with keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for seg in range((len(segments) - 1), 0, -1):                 //Previous Code without OOP
    #     new_x = segments[seg - 1].xcor()
    #     new_y = segments[seg - 1].ycor()
    #     segments[seg].goto(new_x, new_y)

    # segments[0].forward(20)

    #Moving the Snake
    snake.move()

    #Detect collisions with food & Extend Snake
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.inc_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1::]:                         #Slicing the segments
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()