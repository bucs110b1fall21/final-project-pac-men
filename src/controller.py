import pygame
from pacmanclass import *
from enemyclass import *
from config import *

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.player = Player(PLAYER_START_POSITION)
    vec = pygame.math.Vector2
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
