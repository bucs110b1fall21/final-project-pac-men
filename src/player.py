import pygame
#from config import *
from pygame.math import Vector2 as vec

class Pacman:

    def __init__(self, Controller, coordinates):
        self.Controller = Controller
        self.coordinates = coordinates
        self.pixel_position = self.get_position()
        self.freetoMove = True
        self.score = 0
        self.direction = vec(1,0)
        self.queued_direction = None
        self.lives = 1
        print(self.coordinates)
        print(self.pixel_position)


    def get_position(self):
        return vec(self.coordinates.x*self.controller.box_width, self.coordinates.y*self.controller.box_height)

    def draw(self):
        pygame.draw.circle(self.controller.screen, (190, 194, 15), (int(self.pixel_position.x), int(self.pixel_position.y)), 8)

    def update(self):
        if self.freetoMove:
            self.pixel_position += self.direction
       # if self.centered:
           # if self.queued_direction != None:
              #  self.direction = self.queued_direction
            self.freetoMove =  self.noCollision

        self.coordinates.x = (self.pixel_position.x +
                            self.controller.box_width//2)//self.controller.box_width+1
        self.coordinates.y = (self.pixel_position.y +
                            self.controller.box_height//2)//self.controller.box_height+1
                            
        #if self.coin():
            #self.eat()

    def move(self, direction):
        self.direction = direction

    #def coin(self):
        #if self.coordinates in self.controller.coin:
            #if self.centered == True:
                #return True

    #def eat(self):
        #self.controller.coins.remove(self.coordinates)

    def noCollision(self):
        for boundary in self.controller.boundaries:
            if vec(self.coordinates+self.direction) == boundary:
                return False
        return True

    def centered(self):
        if int(self.pixel_position) % self.controller.box_width == 0:
            if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
                return True
        if int(self.pixel_position.y) % self.controller.box_height == 0:
            if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
               return True
        return False