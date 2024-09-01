import tkinter as tk
from tkinter import font
import subprocess
from multiprocessing import Process
from tkinter import PhotoImage
from playsound import playsound

def play_sound():
    playsound("audio.mp3")

def open_snake_game():
    sound_process.terminate()
    root.iconify()
    process = subprocess.Popen(["python", "snakegame/main95.py"])
    process.wait()
    root.deiconify()
    restart_sound()

def open_pong_game():
    sound_process.terminate()
    root.iconify()
    process = subprocess.Popen(["python", "ponggame/main25.py"])
    process.wait()
    root.deiconify()
    restart_sound()

def open_road_crossing_turtle_game():
    sound_process.terminate()
    root.iconify()
    process = subprocess.Popen(["python", "roadcrossingturtle/main45.py"])
    process.wait()
    root.deiconify()
    restart_sound()

def open_alien_space_invader():
    sound_process.terminate()
    root.iconify()
    process = subprocess.Popen(["python", "alienspaceinvader/main42.py"])
    process.wait()
    root.deiconify()
    

def open_rock_paper_scissor():
    sound_process.terminate()
    root.iconify()
    process = subprocess.Popen(["python", "rock paper scissor/main00.py"])
    process.wait()
    root.deiconify()
    

def restart_sound():
    global sound_process
    sound_process = Process(target=play_sound)
    sound_process.start()

    

if __name__ == '__main__':
    global root, sound_process
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Canvas Example")

    sound_process = Process(target=play_sound)
    sound_process.start()

    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack(fill="both", expand=True)

    bg_image = tk.PhotoImage(file="source image/vectorimage.png")
    canvas.create_image(0, 0, anchor='nw', image=bg_image)

    crackman_font = font.Font(family='CrackMan', size=24)
    canvas.create_text(250, 50, text="Welcome to the game script", font=crackman_font, fill='white')

    button_frame = tk.Frame(canvas, bg='lightgrey')
    snake_image = PhotoImage(file="source image/button.png")
    pong_image = PhotoImage(file="source image/pong.png")
    road_image = PhotoImage(file="source image/roadcross.png")
    alien_image = PhotoImage(file="source image/alien.png")
    rps_image = PhotoImage(file="source image/rps.png")


    button1 = tk.Button(canvas, image=snake_image, command=open_snake_game)
    button2 = tk.Button(canvas, image=pong_image, command=open_pong_game)
    button3 = tk.Button(canvas, image=road_image, command=open_road_crossing_turtle_game)
    button4 = tk.Button(canvas, image=alien_image, command=open_alien_space_invader)
    button5 = tk.Button(canvas, image=rps_image, command=open_rock_paper_scissor)

    button1.place(x=150, y=100)
    button2.place(x=155, y=150)
    button3.place(x=90, y=200)
    button4.place(x=130, y=250)
    button5.place(x=150, y=300)

    canvas.create_window(250, 300, window=button_frame, anchor='n')
    root.resizable(0, 0)
    
    root.mainloop()
    sound_process.terminate()