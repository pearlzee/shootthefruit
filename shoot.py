# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:22:21 2019

@author: Pearl
"""
import pgzrun

# initialise screen
#games.init(screen_width = 640, screen_height = 480, fps = 50)

#import os
#from os.path import dirname, realpath, abspath

#__file__ = "D:/Technology/python/pygame/pallavi/shootthefruit"    # <-- This code is needed for CX_freeze, to avoid NameError.
#file_path = os.path.join(dirname(__file__), "images", "apple.png")
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()
    
def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)
    

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()
        
    
place_apple()
   

pgzrun.go()