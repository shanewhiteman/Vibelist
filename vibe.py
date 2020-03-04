import os
import pygame
from tkinter import *

class Player:
    # def __init__(self, master=None):
    #     Frame.__init__(self, master)               
    #     self.master = master

    # Def Window
    def __init__(self,root):
        self.root = root
        self.root.title("Vibe") # Title of the window
        self.root.geometry("1000x200+200+200") # Window Geometry

        pygame.init() # Initiating Pygame
        pygame.mixer.init() # Initiating Pygame Mixer

        self.track = StringVar() # Declaring track Variable
        self.status = StringVar() # Declaring Status Variable
        #self.pack(fill=BOTH, expand=1) # take full space of the root window

        quitButton = Button(self, text="Quit") # creating a button instance
        quitButton.place(x=0, y=0) # placing the button on my window

root = Tk()

root.geometry("400x300") #size of the window


app = Player(root)
root.mainloop() 