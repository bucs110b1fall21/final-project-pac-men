#import your controller

import pygame

def main():
    pygame.init()
    team = {"lead": "Jason Lin", "backend": "Nicholas Tavormina", "frontend": "Axin Li"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])
main()

