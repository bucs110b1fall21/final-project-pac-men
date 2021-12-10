import pygame
from .config import *
from pygame.math import Vector2 as vec

class Pacman:

    def __init__(self, Controller, coordinates):
        """
        Constructor. Initilizes the amount of lives, sets the default value for self.freetoMove to be true, sets the pixel position of pacman to the result of getPosition(), sets a default direction vector value, etc. Creates instance variables for pacman to be used in the controller.
        Controller (class) Controller class is called. Used to work with the controller for drawing on the screen, grabbing screen data, and acessing the boundaries layout to be used with the player
        coordinates (variable) Vector grid location of pacman (player) passed throuugh as self.pacmanposition
        return : N/A
        """
        self.Controller = Controller
        self.coordinates = coordinates
        self.pixel_position = self.getPosition()
        #self.freetoMove = True
        self.score = 0
        self.direction = vec(1,0)
        #self.queued_direction = None
        self.lives = 1

    def draw(self):
        """
        Method that draws pacman on the screen with a yellow color, specified pixel position, and width.
        """
        pygame.draw.circle(self.Controller.screen, PACMAN_COLOR, (int(self.pixel_position.x), int(self.pixel_position.y)), WIDTH)

    def update(self):
        """
        Update method. Handles all the movement operations for pacman. Also sets the relationship between a grid positioning system and pixel positioning system. Also eats a coin
        """
        if self.noCollision:
            self.pixel_position += self.direction*SPEED
        if self.coin():
            self.eat()

        self.coordinates.x = (self.pixel_position.x +
                            self.Controller.box_width//2)//self.Controller.box_width+1
        self.coordinates.y = (self.pixel_position.y +
                            self.Controller.box_height//2)//self.Controller.box_height+1
                            
    def getPosition(self):
        """
        Method that calculates a pixel position vector value given an object grid-based coordinates. Uses the "boxes" of the screen (grid).
        Return : Vector value to be used as the object's pixel position
        """
        return vec(self.coordinates.x*self.Controller.box_width, self.coordinates.y*self.Controller.box_height)

    def move(self, direction):
        """
        Updates direction based on user input
        """
        self.direction = direction

    def coin(self):
        """
        Method that checks whether or not pacman is on a coin. Uses the coordinates system (grid).
        return: (boolean) True/False statement deciding whether or not pacman is one a coin.
        """
        if self.coordinates in self.Controller.coins:
            if self.centered == True:
                return True

    def eat(self):
        """
        Method that, if pacman is on a coin, removes the coin from the list. 
        """
        self.Controller.coins.remove(self.coordinates)

    def noCollision(self):
        """
        Method that checks for collison by comparing the player's grid position to the boundry position from boundaries.txt
        return: (boolean) True/False statement. False if there is a collision, true if there isn't one.
        """
        print(self.boundaries)
        for boundaries in self.Controller.boundaries:
            if vec(self.coordinates+self.direction) == boundaries:
                print("False")
                return False
        return True
        print("True")

    def centered(self):
        """
        Method that checks if the player's pixel position is in the middle of the "grid" by comparing it to the "box" size. Does this for both the x-axis and y-axis. Prevents pac-man from moving mid box.
        return: (boolean) True/False statement. Returns true if the player is centered within the box/grid.
        """
        if int(self.pixel_position) % self.Controller.box_width == 0:
            if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
                return True
        if int(self.pixel_position.y) % self.Controller.box_height == 0:
            if self.direction ==  vec(1,0) or self.direction == (-1,0) or self.direction == vec(0,0):
               return True
        return False