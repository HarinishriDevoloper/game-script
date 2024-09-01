from turtle import Screen
import time
import playsound
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgpic("image/pong image.png")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball =Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

def ball_crash():
    playsound.playsound("uu.mp3",False)

game_is_on=True
while game_is_on:   
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    


    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
        ball_crash()
        

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 ) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball_crash()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball_crash()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball_crash()

screen.exitonclick()