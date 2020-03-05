import os
import pygame
from tkinter import *

# Add shuffle, repeat, and queue functions
# Elaborate on the song finding fuction?

class MusicPlayer:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Music Player")
        self.frame.geometry("1000x200")

        pygame.init()
        pygame.mixer.init()

        self.track = StringVar()
        self.status = StringVar()

        # Track frame for song label & status label
        trackframe = LabelFrame(self.frame, text="Song Track", font=("verdana", 17, "bold"), bg="white", fg="maroon", bd=5, relief=GROOVE)
        trackframe.place(x=400, y=0, width=600, height=100)
        # Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("verdana", 24, "bold"), bg="white", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Status Label
        trackstatus = Label(trackframe, textvariable=self.status, font=("verdana", 24, "bold"), bg="white", fg="gold").grid(row=0, column=1, padx=10, pady=5)
        # Button Frame
        buttonframe = LabelFrame(self.frame,text="Control", font=("verdana", 17, "bold"), bg="white", fg="maroon", bd=5, relief=SUNKEN)
        buttonframe.place(x=400, y=100, width=600, height=100)
        # Executable Buttons
        play_btn = Button(buttonframe, text="PLAY", command=self.Play, width=6, height=1, font=("verdana", 16, "bold"), fg="dodger blue",bg="gold").grid(row=0, column=0, padx=10, pady=5)
        pause_btn = Button(buttonframe, text="PAUSE", command=self.Pause, width=8, height=1, font=("verdana", 16, "bold"), fg="dodger blue",bg="gold").grid(row=0, column=1, padx=10, pady=5)
        unpause_btn = Button(buttonframe, text="UNPAUSE", command=self.Unpause, width=10, height=1,font=("verdana", 16, "bold"), fg="dodger blue",bg="gold").grid(row=0, column=2, padx=10, pady=5)
        stop_btn = Button(buttonframe, text="STOP", command=self.Stop, width=6, height=1, font=("verdana", 16, "bold"), fg="dodger blue",bg="gold").grid(row=0, column=3, padx=10, pady=5)
        # Playlist Frame
        songsframe = LabelFrame(self.frame, text="Music List", font=("verdana", 17, "bold italic"), bg="white", fg="maroon", bd=5, relief=GROOVE)
        songsframe.place(x=0, y=0, width=400, height=200)
        # Scrollbar
        scrol_y = Scrollbar(songsframe ,orient=VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold",selectmode=SINGLE, font=("verdana",12, "bold"), bg="maroon", fg="dodger blue", bd=5, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Song Folder
        os.chdir("/Users/shanewhiteman/Desktop/playlist")
        # Fetching Songs
        songtracks = os.listdir()
        # Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    def Play(self):
        self.track.set(self.playlist.get(ACTIVE)) #Display song title
        self.status.set("Playing")

        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def Stop(self):
        self.status.set("Stopped")
        pygame.mixer.music.stop()

    def Pause(self):
        self.status.set("Paused")
        pygame.mixer.music.pause()

    def Unpause(self):
        self.status.set("Playing")
        pygame.mixer.music.unpause()

frame = Tk()
MusicPlayer(frame)
frame.mainloop()