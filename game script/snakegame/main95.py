from turtle import Screen, Turtle
from food import Food
from score import Scoreboard
import time
from snake2 import Snake
from sound import Playsound


screen=Screen()
screen.title("snake game")
image_width=600
image_height=600
screen.setup(width=image_width,height=image_height)
screen.bgpic("image/snake board.png")
screen.tracer(0)
food = Food()
score = Scoreboard()

snake=Snake()
screen.listen()
screen.onkeypress(key="Up",fun=snake.go_up)
screen.onkeypress(key="Down",fun=snake.go_down)
screen.onkeypress(key="Right",fun=snake.go_right)
screen.onkeypress(key="Left",fun=snake.go_left)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food)<30):
        food.refresh()
        score.increase_score()
        snake.extend()
        Playsound.catch_food()
      
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over()
        Playsound.game_close()
    for segment in snake.segments:
        if segment ==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()
          
          
    
screen.exitonclick()