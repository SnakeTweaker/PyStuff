'''1280x960 Window source code for easy copying into python games'''
import pygame, sys

#General setup
pygame.init()
clock = pygame.time.Clock()

#setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('1280x960 Window')

while True:
    #Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #updating window 60 fps
    pygame.display.flip()
    clock.tick(60)
