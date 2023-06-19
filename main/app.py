#music Player

#modules

import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog 
from pygame import mixer

#creating app

root = Tk()

#properties

root.geometry("920x600")
root.title("Music Player")
root.config(background="#212121")
root.resizable(False, False)

image_icon = PhotoImage(file="MUSIC_LOGO.png")

taskbar_icon = PhotoImage(file="taskbar_music_logo.png")

root.iconphoto(False, image_icon, taskbar_icon)

root.iconbitmap("E:\Visual Basic\MUSIC_LOGO.ico")

#initialize

mixer.init()

#functions [music]

def AddMusic():
    
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# logo

logo = PhotoImage(file="MUSIC_LOGO.png")
Label(root, image=logo, bg="#0f1a2b", bd=0).place(x=70, y=115)

#Label 

Menu = PhotoImage(file="music_backdrop.png")
Label(root, image= Menu, bg="#0f1a2b").pack(padx=10 , pady= 50 , side= RIGHT)

Frame_Music = Frame(root , bd= 2, relief= RIDGE)
Frame_Music.place(x= 330 , y= 300 , height= 250 , width= 560)

Button(root, text="Open Folder", width= 15 , height= 2, font=("Calibri", 12 , ""), fg="Black", bg= "#21b3de", 
       command= AddMusic).place(x=330 , y= 250)

Scroll = Scrollbar(Frame_Music)

Playlist = Listbox(Frame_Music, width= 100 , font=("Calibre", 10, ""), bg="#333334", fg="gray", 
                   selectbackground= "#00fffa",
                   cursor= "hand2", bd=0, yscrollcommand= Scroll.set)

Scroll.config(command= Playlist.yview)
Scroll.pack(side= RIGHT, fill= Y)
Playlist.pack(side= LEFT, fill= BOTH)

#controls

ButtonPlay = PhotoImage(file="start.png")
Button(root, image=ButtonPlay, bg="#0f1a2b", bd=0, command=PlayMusic).place(x= 50, y= 400)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#0f1a2b", bd= 0, command=mixer.music.stop).place(x= 10 , y= 500)

ButtonResume = PhotoImage(file="Resume.png")
Button(root, image=ButtonResume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=170, y=500)

ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=170, y=400)

#brand

l1 = Label(root, text="Music Player", font=("Calibri", 34, ""))
l1.place(x= 650 , y= 100)

#Execute the App

root.mainloop()