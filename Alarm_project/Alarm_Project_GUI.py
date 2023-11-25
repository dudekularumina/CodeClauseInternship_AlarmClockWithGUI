from tkinter import *
from tkinter import messagebox
import time, sys
from pygame import mixer
from PIL import Image, ImageTk
def playmusic():
    mixer.init()
    mixer.music.load('alarm_sound.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()
def alarm():
    alarm_time=user_input.get()
    current_time=time.strftime("%H:%M")

    while alarm_time !=current_time:
        current_time=time.strftime("%H:%M")

    if(alarm_time==current_time):
          playmusic()


root=Tk()
root.title("Alarm Clock")
root.geometry("800x400")
canvas=Canvas(root, width=800,height=400)
image=ImageTk.PhotoImage(Image.open("alarm.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
header=Frame(root)


Label(root,text="Digital Alarm Clock", bg="lightblue",font="Helvetica 22 bold").place(x=450,y=50)

Label(root,text="Enter Time: ", bg="lightpink", font="Helvetica 19 bold").place(x=410,y=140)
box1=Frame(root)
box1.place(x=560,y=140)
box2=Frame(root)
box2.place(x=480,y=230)

#User Input
user_input=Entry(box1, font=('Arial narrow', 20), width=13)
user_input.grid(row=0, column=2)
#Alarm Button
start_button=Button(box2, text="Set Alarm",bg="lightgreen",font=("Helvetica", 20, "bold"), command=alarm)
start_button.grid(row=2, column=2)

root.mainloop()
