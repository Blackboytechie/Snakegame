from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.title("Snake Game")
s.bgcolor("white")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")
s.onkey(snake.down, "Down")
is_game_on = True

while is_game_on:
    s.update()
    time.sleep(0.2)
    snake.new_seg.speed("fastest")
    snake.move()
    if snake.seg[0].distance(food) < 15:
        food.refresh()
        score.track_points()
        snake.snake_grow()
    if snake.seg[0].xcor() > 280 or snake.seg[0].xcor() < -280 or snake.seg[0].ycor() > 280 or snake.seg[
        0].ycor() < -280:
        score.game_over()
        snake.refresh_snake()
        print("head crashed with wall")
    if snake.check_body_collision():
        print("head crashed with body")
        score.game_over()
        snake.refresh_snake()
print("while loop ended")
s.exitonclick()
