# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:22:21 2019

@author: Pearl
"""
#import what we need
import pygame,sys
from pygame.locals import *
from random import randint

#set up pygame
pygame.inti()

#set up window
windowSurface = pygame.display.set_mode((500,400),0,32)

pygame.display.set_caption('Hello')

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
   

pygame.go()
