import pygame
import random
#from config import *
from pygame.math import Vector2 as vec


class Ghosts:
    def __init__(self, controller, coordinates, identity):
        self.controller = controller
        self.coordinates = coordinates
        self.pixel_position = self.get_position()
        self.direction = vec(0,0)
        self.chase = None
       # self.color = self.setColor()
        self.identity = identity
    
    def draw(self):
        pygame.draw.circle(self.controller.screen, (75, 50, 84), int(self.pixel_position.x), int(self.pixel_position.y), 8)

    def update(self):
        self.pixel_position + self.direction
    #    if self.Centered():
        self.randomMovement()

     #   def Centered(self):
     #       if int(self.pixel_position) % self.controller.box_width == 0:
      #      if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
      #          return True
      #  if int(self.pixel_position.y) % self.controller.box_height == 0:
      #      if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
      #         return True
      #  return False

   # def setColor(self):
     #   if self.identity == 4:
     #       return (100, 200, 30)
     #   if self.identity == 3:
      #      return (75, 50, 84)
     #   if self.identity == 2:
      #      return (200, 100, 3)
      #  if self.identity == 1:
     #       return (34, 159, 103)

    def randomMovement(self):
        self.direction = self.randomDirection()

    def randomDirection(self):
        number = random.randint(-2, 1)
        if number == -2:
            xdirection, ydirection = 1, 0
        elif number == -1:
            xdirection, ydirection = 0, 1
        elif number == 0:
            xdirection, ydirection = -1, 0
        else:
            xdirection, ydirection = 0, -1
        queuedposition = vec(self.coordinates.x + xdirection, self.coordinates.y + ydirection)
        if queuedposition not in self.controller.boundaries:
            return vec(xdirection, ydirection)

    def get_position(self):
        return vec(self.coordinates.x*self.controller.box_width, self.coordinates.y*self.controller.box_height)
