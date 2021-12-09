import pygame
import sys
from pacmanclass import *
from enemyclass import *
from config import *


class Controller:

    def __init__(self):
        # setup pygame data
        self.window_width = 900
        self.window_height = 600
        self.state = 'GAME'
        vec = pygame.math.Vector2
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.background.fill((250, 250, 250))

        # configure pygame

        # held keys are repeated
        pygame.key.set_repeat(50, 500)

        # call font to use
        pygame.font.init()

        self.player = Player(PLAYER_START_POSITION)
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))

    def mainloop(self):
        # check for events
        while True:
            if (self.state == 'GAME'):
                self.gameloop()
            elif (self.state == 'GAMEOVER'):
                self.gameoverloop()

    # select state loop

    ### below are some sample loop states ###

    def menuloop(self):

    # event loop

    # update data

    # redraw

    # update the screen

    def gameloop(self):
        # event loop
        while self.state == 'GAME':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP):
                        self.player.move("U")
                    elif (event.key == pygame.K_DOWN):
                        self.player.move("D")
                    elif (event.key == pygame.K_LEFT):
                        self.player.move("L")
                    elif (event.key == pygame.K_RIGHT):
                        self.player.move("R")
        # update data

        # check for collisions

        # redraw
        self.enemies.update()
        self.screen.blit(self.background, (0, 0))
        if (self.player.health == 0):
            self.state = 'GAMEOVER'
        self.all_sprites.draw(self.screen)
        # update the screen
        pygame.display.flip()


def gameoverloop(self):
    self.player.kill()
    # event loop
    myfont = pygame.font.SysFont(None, 30)
    # update data
    if self.player.health == 0:
        self.background.fill((250, 0, 0))
        message = myfont.render('Game Over', False, (0, 0, 0))
    else:
        self.background.fill((0, 250, 0))
        message = myfont.render('You Win', False, (0, 0, 0))
    self.screen.blit(self.background, (0, 0))
    self.screen.blit(message, (self.window_width / 2, self.window_height / 2))

    # redraw
    pygame.display.flip()
