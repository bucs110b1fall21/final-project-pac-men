import pygame
import sys
import copy
from pygame.math import Vector2 as vec
from src import player
from src import enemies
from src import config


class Controller:

    def __init__(self):
        # initializes pac man, the enemies, the background, the loading function, and attempts to instantiate the player and ghost objects
        pacman = player.Pacman
        ghosts = enemies.Ghosts
        self.state = "In-Game"
        self.screen = pygame.display.set_mode((600, 700))
        self.running = True
        pygame.init()
        self.background = pygame.image.load('maze.png')
        self.loading()
        self.pacmanposition = vec(20, 25)
        self.ghostpositions = []
        self.pacman = pacman(self, self.pacmanposition)
        self.ghosts = ghosts(self, vec(1, 1), 1)
        # self.spawnEnemy()

    def loading(self):
        # initializes a few idexes for the list of ghosts, walls and coins. also (attempts) to process the walls on the map
        self.box_width = 600 // 30
        self.box_height = 700 // 28
        self.boundaries = []
        self.coins = []
        self.ghosts = []
        self.walls = []
        with open("boundaries.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.boundaries.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))

    def drawMaze(self):
        for i in range(config.SCREEN_WIDTH // self.box_width):
            pygame.draw.line(self.background, config.BLACK, (i * self.box_width, 0),
                             (i * self.box_width, config.SCREEN_HEIGHT))
        for i in range(config.SCREEN_HEIGHT // self.box_height):
            pygame.draw.line(self.background, config.BLACK, (0, i * self.box_height),
                             (config.SCREEN_WIDTH, i * self.box_height))

    # resets game when lost
    # def reset(self):
        # self.pacman.lives = 1


    def mainloop(self):
        # sets up the three different game states. currently stuck on the first menu for some reason
        while self.running == True:
            if self.state == "Initialization":
                self.menuEvents()
                self.menuDraw()
                self.drawMaze()
            if self.state == "In-Game":
                self.gameEvents()
                self.gameUpdate()
                self.gameDraw()
            elif self.state == "Game-Over":
                self.gameoverloop()
            else:
                self.running = False

    def menuEvents(self):
        # main menu event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state == "In-Game"
                print("space")
                print(self.state)

    def menuDraw(self):
        # push space bar drawing
        self.type('PUSH SPACE BAR', self.screen, [
            800 // 2, 600 // 2 - 50], 15, (170, 132, 58), "arial black", centered=True)
        pygame.display.update()

    def type(self, characters, screen, pos, size, color, font_name, centered=True):
        # pygame typing function
        font = pygame.font.SysFont(font_name, size)
        text = font.render(characters, False, color)
        text_size = text.get_size()
        screen.blit(text, pos)

    # def spawnEnemy(self):
    # for identity in range(4):
    # self.ghosts.append(Enemies(self, vec(-1,0), identity))

    def gameEvents(self):
        # movement of pacman
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
        # updates pacmans movements and begins to layout how the ghosts update
        self.pacman.update()
        for i in range(4):
            self.ghosts.update()
        # checks if pacmans position is the same as the enemys', if so, pacman loses a life
        # for i in range(4):
        # if self.ghostpositions == self.pacmanposition:
        # self.                          # pacman losing life

    def gameDraw(self):
        # draws pacman and the game screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (25, 25))
        self.pacman.draw()
        for i in range(4):
            self.ghosts.draw()
        pygame.display.update()

    def loseCondition(self):
        # beginning of play lives function to game over state
        if self.pacman.lives == 0:
            self.state == "Game-Over"

    def gameoverloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESPACE:
                self.ruunning = False
    # event loop

    # update data

    # redraw"

