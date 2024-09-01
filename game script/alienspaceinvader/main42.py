import turtle
import random
import time
import playsound

window = turtle.Screen()
window.setup(500, 700)
window.bgpic("image/alien imageee.png")
window.title("The Real Python Space Invaders")
window.tracer(0)


def laser_shoot():
    playsound.playsound("laser.mp3",False)
    

def bomb_shoot():
    playsound.playsound("crash.mp3",False)


ALIEN_SPAWN_INTERVAL = 1.2
LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.8 * BOTTOM
CANNON_STEP = 10
GUTTER = 0.025 * window.window_width()
LASER_LENGTH = 20
LASER_SPEED = 10
ALIEN_SPEED = 1
lasers = []
aliens = []

# Create laser cannon
cannon = turtle.Turtle()
cannon.penup()
cannon.color("black")
cannon.shape("square")
cannon.setposition(0, FLOOR_LEVEL)

# Create turtle for writing text
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(LEFT * 0.8, TOP * 0.8)
text.color(1, 1, 1)

# Create turtle for displaying score
score_text = turtle.Turtle()
score_text.penup()
score_text.hideturtle()
score_text.setposition(RIGHT * 0.5, TOP * 0.8)
score_text.color(1,1,1)

score = 0

# def game_close():
#     playsound.playsound("get.mp3",False)

def update_score():
    score_text.clear()
    score_text.write(
        f"Score: {score}",
        font=("Courier", 20, "bold"),
        align="center"
    )

def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(1.5)
    alien.setposition(
        random.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER),
        ),
        TOP,
    )
    alien.shape("turtle")
    alien.setheading(-90)
    alien.color(random.random(), random.random(), random.random())
    aliens.append(alien)

def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    # laser.hideturtle()
    laser.setposition(cannon.xcor(), cannon.ycor())
    laser.setheading(90)
    laser.forward(90)
    laser.pendown()
    laser.pensize(8)
    laser.speed("slow")
    lasers.append(laser)

def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)  # Base
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)  # Next tier
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)  # Tip of cannon
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)
    window.update()

def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    # Draw the laser
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)

def move_left():
    new_x = cannon.xcor() - CANNON_STEP
    if new_x >= LEFT + GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def move_right():
    new_x = cannon.xcor() + CANNON_STEP
    if new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def remove_sprite(sprite, sprite_list):
    sprite.clear()
    sprite.hideturtle()
    window.update()
    sprite_list.remove(sprite)
    turtle.turtles().remove(sprite)

window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(turtle.bye, "q")
window.onkeypress(create_laser, "space")
window.listen()

draw_cannon()
update_score()

alien_timer = 0
game_timer = time.time()
game_running = True
while game_running:

    time_elapsed = time.time() - game_timer
    text.clear()
    text.write(
        f"Time: {time_elapsed:5.1f}s",
        font=("Courier", 20, "bold"),
    )
    # Move all lasers
    for laser in lasers:
        move_laser(laser)
        if laser.ycor() > TOP:
            remove_sprite(laser, lasers)
            laser_shoot()
            break
            

        for alien in aliens:
            if laser.distance(alien) < 20:
                score += 1
                update_score()
                remove_sprite(laser, lasers)
                remove_sprite(alien, aliens)
                bomb_shoot()
                break

    if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = time.time()

    for alien in aliens:
        alien.forward(ALIEN_SPEED)
        # if alien.ycor()<FLOOR_LEVEL:
            # game_running=False
            # game_close()
            # break

    window.update()

splash_text = turtle.Turtle()
splash_text.hideturtle()
splash_text.color(1, 1, 1)
splash_text.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
turtle.done()