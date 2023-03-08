import pygame
from sys import exit
import config

pygame.init()
screen = pygame.display.set_mode(config.screenSize)
pygame.display.set_caption(config.screenName)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()


