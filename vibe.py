import os
from tkinter import *

import pygame

# Add shuffle, repeat, and queue functions
# Elaborate on the song finding fuction?


class MusicPlayer:
    def __init__(self, frame: Tk, playlist_dir: str):
        self.frame = frame
        self.frame.title("Music Player")
        self.frame.geometry("1000x200")

        pygame.mixer.init()

        self.track = StringVar()
        self.status = StringVar()
        self.playlist = None

        self._draw_track_frame()
        self._draw_playlist_frame()
        self._draw_control_frame()

        os.chdir(playlist_dir)
        songtracks = os.listdir()

        # Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    def _draw_control_frame(self):

        buttonframe = LabelFrame(self.frame, text="Control", font=(
            "verdana", 17, "bold"), bg="white", fg="maroon", bd=5, relief=SUNKEN)
        buttonframe.place(x=400, y=100, width=600, height=100)

        # play button
        Button(buttonframe, text="PLAY", command=self.play, width=6, height=1, font=(
            "verdana", 16, "bold"), fg="dodger blue", bg="gold").grid(row=0, column=0, padx=10, pady=5)
        # pause button
        Button(buttonframe, text="PAUSE", command=self.pause, width=8, height=1, font=(
            "verdana", 16, "bold"), fg="dodger blue", bg="gold").grid(row=0, column=1, padx=10, pady=5)
        # unpause button
        Button(buttonframe, text="UNPAUSE", command=self.unpause, width=10, height=1, font=(
            "verdana", 16, "bold"), fg="dodger blue", bg="gold").grid(row=0, column=2, padx=10, pady=5)
        # stop button
        Button(buttonframe, text="STOP", command=self.stop, width=6, height=1, font=(
            "verdana", 16, "bold"), fg="dodger blue", bg="gold").grid(row=0, column=3, padx=10, pady=5)

    # draw track frame for song label & status label
    def _draw_track_frame(self):
        trackframe = LabelFrame(self.frame, text="Song Track", font=(
            "verdana", 17, "bold"), bg="white", fg="maroon", bd=5, relief=GROOVE)
        trackframe.place(x=400, y=0, width=600, height=100)

        # Song Track Label
        Label(trackframe, textvariable=self.track, width=20, font=(
            "verdana", 24, "bold"), bg="white", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Status Label
        Label(trackframe, textvariable=self.status, font=(
            "verdana", 24, "bold"), bg="white", fg="gold").grid(row=0, column=1, padx=10, pady=5)

    # draw playlist frame
    def _draw_playlist_frame(self):
        songsframe = LabelFrame(self.frame, text="Music List", font=(
            "verdana", 17, "bold italic"), bg="white", fg="maroon", bd=5, relief=GROOVE)
        songsframe.place(x=0, y=0, width=400, height=200)

        # scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=(
            "verdana", 12, "bold"), bg="maroon", fg="dodger blue", bd=5, relief=GROOVE)

        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

    def play(self):
        self.track.set(self.playlist.get(ACTIVE))  # Display song title
        self.status.set("Playing")

        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stop(self):
        self.status.set("Stopped")
        pygame.mixer.music.stop()

    def pause(self):
        self.status.set("Paused")
        pygame.mixer.music.pause()

    def unpause(self):
        self.status.set("Playing")
        pygame.mixer.music.unpause()


def main():

    if len(sys.argv) < 2:
        print("Usage: Vibelist <playlist directory>")
        sys.exit(1)

    playlist = sys.argv[1]

    frame = Tk()
    MusicPlayer(frame, playlist)
    frame.mainloop()


main()
