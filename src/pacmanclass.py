import pygame
from settings import *

class Player:

    def __init__(self, controller, coordinates):
        self.controller = controller
        self.starting_position = [coordinates.x, coordinates.y]
        self.grid_position = coordinates
        self.pixel_position = self.get_position()
        self.can_move = True
        self.score = 0
        self.direction = vec(1,0)


    def get_position(self):
        return vec(self.grid_position.x*self.controller.box_width, self.grid_position.y*self.controller.box_height)

    def draw(self):
        # Drawing Pac-Man
        pygame.draw.circle(self.controller.screen, PLAYER_COLOR, (int(self.pixel_position.x), int(self.pixel_position.y)), width)

    def update(self):
        self.pixel_position += self.direction

    


    def move(self, direction):
        self.direction = direction