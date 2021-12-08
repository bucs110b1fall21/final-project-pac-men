import pygame
import random
from settings import *

class Enemy:
    def __init__(self, controller, coordinates, idenity):
        self.starting_positon = [coordinates.x, coordinates.y]
        self.controller = controller
        self.grid_position = coordinates
        self.pixel_position = self.get_position()
        self.color = self.set_color()
    
    def update(self):
        pass


    def set_color(self):
        
