import pygame
from pygame.locals import *
from config import *
import snake

pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption(screenName)
clock=pygame.time.Clock()
RED = (255, 0, 0)

rect = Rect(50, 60, 200, 80)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.draw.rect(screen, RED, rect)
    clock.tick(framerate)


pygame.quit()


