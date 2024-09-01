
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import playsound

screen=Screen()
screen.title("Road crossing tutrle")
screen.setup(width=600, height=600)
screen.bgpic("image/road.png")
screen.tracer(0)

player=Player() 
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

def game_close():
    playsound.playsound("get.mp3",False)
    


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
   
    

    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            game_close()

                                                                
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
