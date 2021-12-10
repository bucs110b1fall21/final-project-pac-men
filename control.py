import pygame
import sys
from pygame.math import Vector2 as vec
from src import player
from src import enemies
from src import config


class Controller:

    def __init__(self):
        ''' Initializes the game the sprites Pacman and the Ghosts. Sets the default value of
         background as 600x700 and displays the maze.png. Also Pacman will always be in a moving state until the game ends
         with self.running. '''
        pacman = player.Pacman
        ghosts = enemies.Ghosts
        self.state = "In-Game"
        self.screen = pygame.display.set_mode((600, 700))
        self.running = True
        pygame.init()
        self.background = pygame.image.load('maze.png')
        self.loading()
        self.pacmanposition = vec(21, 4)
        self.enemies = []
        self.ghostpositions = []
        self.pacman = pacman(self, self.pacmanposition)

    def loading(self):
        '''Opens the boundaries.txt file and creates the walls list with coordinates
        of the walls by storing it as a vector. Also makes the box_width and box_height
        for when a grid is made.'''
        self.box_width = 600 // 30
        self.box_height = 700 // 28
        self.walls = []
        self.coins = []
        self.ghosts = []
        self.boundaries = []
        with open("boundaries.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))

    def make_Ghosts(self):
        for idx, pos in enumerate(self.ghostpositions):
            self.enemies.append(enemies.Ghosts(self, vec(pos), idx))

    def drawMaze(self):
        ''' Creates the maze or grid using the box_width and box_height.'''
        for i in range(config.SCREEN_WIDTH // self.box_width):
            pygame.draw.line(self.background, config.BLACK, (i * self.box_width, 0),
                             (i * self.box_width, config.SCREEN_HEIGHT))
        for i in range(config.SCREEN_HEIGHT // self.box_height):
            pygame.draw.line(self.background, config.BLACK, (0, i * self.box_height),
                             (config.SCREEN_WIDTH, i * self.box_height))

    def reset(self):
        '''Resets the game once Pacman touches a Ghost.'''
        self.pacman.lives = 1
        self.pacman.coordinates = vec(self.pacman.starting_pos)
        self.pacman.pixel_position = self.pacman.getPosition()

    def mainloop(self):
        '''Sets up the three game states, menu, playing the game, and the end screen. Currently
        the game is stuck on the In-Game state. '''
        while self.running == True:
            if self.state == "Initialization":
                self.menuEvents()
                self.menuDraw()
                self.drawMaze()
            elif self.state == "In-Game":
                self.gameEvents()
                self.gameUpdate()
                self.gameDraw()
            elif self.state == "Game-Over":
                self.gameoverloop()
            else:
                self.running = False
        pygame.quit()
        sys.exit()

    def menuEvents(self):
        ''' The main menu screen and pressing space starts the game.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "In-Game"
                print("space")
                print(self.state)

    def menuDraw(self):
        ''' Creates text that says "PUSH SPACE BAR" in the center of the screen.'''
        self.type('PUSH SPACE BAR', self.screen, [
            800 // 2, 600 // 2 - 50], 15, (170, 132, 58), "arial black", centered=True)
        pygame.display.update()

    def type(self, characters, screen, pos, size, color, font_name, centered=True):
        '''Method used for the pygame.type function'''
        font = pygame.font.SysFont(font_name, size)
        text = font.render(characters, False, color)
        text_size = text.get_size()
        screen.blit(text, pos)

    def gameEvents(self):
        '''Creates the movement of Pacman with arrow keys'''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.pacman.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.pacman.move(vec(0, -1))
                if event.key == pygame.K_LEFT:
                    self.pacman.move(vec(-1, 0))
                if event.key == pygame.K_DOWN:
                    self.pacman.move(vec(0, 1))

    def gameUpdate(self):
        '''Updates the movement of Pacman'''
        self.pacman.update()

    def gameDraw(self):
        '''Draws Pacman and the game screen'''
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (25, 25))
        self.pacman.draw()
        pygame.display.update()

    def loseCondition(self):
        '''Initializes the Game-Over state of the game.'''
        if self.pacman.lives == 0:
            self.state = "Game-Over"

    def gameoverloop(self):
        '''Game over state oef the game'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESPACE:
                self.running = False
