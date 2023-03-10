import pygame
import config
import snake




pygame.init()
screen = pygame.display.set_mode(config.screenSize)
pygame.display.set_caption(config.screenName)
clock=pygame.time.Clock()

keys = pygame.key.get_pressed()
s=snake.Snake()
a=snake.Apple()



running = True
while running:
    screen.fill("Black")
    s.switchScreen()
    s.move()
    s.print(screen)
    s.death()
    a.collide(s)
    a.print(screen)
    pygame.display.update()


    clock.tick(config.framerate)


pygame.quit()

