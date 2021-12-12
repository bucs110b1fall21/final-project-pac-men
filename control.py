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
        self.state = "Initialization"
        self.screen = pygame.display.set_mode((610, 670))
        self.maze_width = 560 // 28
        self.maze_height = 620 // 30
        self.running = True
        pygame.init()
        self.background = pygame.image.load('maze.png')
        self.loading()
        self.pacmanposition = vec(21, 4)
        self.ghosts = enemies.Ghosts
        self.ghostpositions = vec(15, 15)
        self.ghost = ghosts(self, self.ghostpositions)
        self.pacman = pacman(self, self.pacmanposition)

    def loading(self):
        '''Opens the boundaries.txt file and creates the walls list with coordinates
        of the walls by storing it as a vector. Also makes the box_width and box_height
        for when a grid is made.'''
        self.box_width = 610 // 28
        self.box_height = 670 // 30
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

    def drawMaze(self):
        ''' Creates the maze or grid using the box_width and box_height.'''
        for i in range(config.SCREEN_WIDTH // self.maze_width):
            pygame.draw.line(self.background, config.WHITE, (i * self.maze_width, 0),
                             (i * self.maze_height, config.SCREEN_HEIGHT))
        for i in range(config.SCREEN_HEIGHT // self.box_height):
            pygame.draw.line(self.background, config.WHITE, (0, i * self.box_height),
                             (config.SCREEN_WIDTH, i * self.box_height))

    '''def makeEnemies(self):
        for idx, pos in enumerate(self.ghostpositions):
            self.ghosts.append(enemies.Ghosts(self, vec(pos), idx))'''

    def reset(self):
        '''Resets the game once Pacman touches a Ghost.'''
        self.pacman.lives = 1
        self.pacman.coordinates = vec(self.pacman.starting_pos)
        self.pacman.pixel_position = self.pacman.getPosition()
        self.pacman.direction *= 0
        self.pacman.grid_pos = vec(self.pacman.starting_pos)
        '''for ghost in self.ghosts:
            ghost.grid_pos = vec(enemies.Ghosts.starting_pos)
            ghost.pixel_position = ghost.getPosition()'''

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
            800 // 2 - 170, 600 // 2 - 50], 15, (170, 132, 58), "arial black", centered=True)
        pygame.display.update()

    def type(self, characters, screen, pos, size, color, font_name, centered=True):
        '''Method used for the pygame.type function'''
        font = pygame.font.SysFont(font_name, size)
        text = font.render(characters, False, color)
        text_size = text.get_size()
        screen.blit(text, pos)

    def drawText(self, txt, screen, pos, size, color, font, centered=False):
        font = pygame.font.SysFont(font, size)
        text = font.render(txt, False, color)
        text_size = text.get_size()
        if centered:
            pos.x = pos.x - text_size[0] // 2
            pos.y = pos.y - text_size[1] // 2
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

    def drawCoins(self):
        for coins in self.coins:
            pygame.draw.circle(self.screen, (124, 123, 7),
                               (int(coins.x * self.maze_width) + self.maze_width // 2 + config.TOP_BOTTOM_BUFFER // 2,
                                int(coins.y * self.maze_height) + self.maze_height // 2 + config.TOP_BOTTOM_BUFFER // 2),
                               5)

    def gameUpdate(self):
        '''Updates the movement of Pacman'''
        self.pacman.update()
        # for i in range(4):
        # self.ghost.update()
        self.ghost.update()
        '''Checks if the ghost coordinates is equal to Pacman's coordinates, if so, Pacman loses a life.'''
        if self.pacmanposition == self.ghostpositions:
            self.loseLife()

    def gameDraw(self):
        '''Draws Pacman and the game screen'''
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (25, 25))
        self.pacman.draw()
        self.drawCoins()
        self.drawText('SCORE: {}'.format(self.pacman.score),
                      self.screen, [60, 0], 18, config.WHITE, config.FONT)
        # for i in range(4):
        # self.ghost.draw()
        self.ghost.draw()
        pygame.display.update()

    def loseCondition(self):
        '''Initializes the Game-Over state of the game.'''
        if self.pacman.lives == 0:
            self.state = "Game-Over"

    def loseLife(self):
        self.pacman.lives -= 1
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
