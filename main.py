import pygame
from config import *
import snake
class snake:

    def __init__(self) -> None:
        self.snake= [pygame.Surface((20,20))]
        self.location=[(40,40)]
        self.directionX=1
        self.directionY=0

    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:   
                if event.key==pygame.K_DOWN:
                    self.directionX=0
                    self.directionY=1
                if event.key==pygame.K_UP:
                    self.directionX=0
                    self.directionY=-1
                if event.key==pygame.K_RIGHT:
                    self.directionX=1
                    self.directionY=0
                if event.key==pygame.K_LEFT:
                    self.directionX=-1
                    self.directionY=0

    def print(self):
        temp=self.snake.pop(0)
        self.snake.append(temp)

        self.location.append((self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY))
        self.location.pop(0)

        for i in range(len(self.snake)):
            self.snake[i].fill('White')
            screen.blit(self.snake[i],self.location[i])
    
    def switchScreen(self):
        if self.location[-1][0]<0:self.location[-1][0]=750
        if self.location[-1][0]>750:self.location[-1][0]=0
        if self.location[-1][1]<0:self.location[-1][1]=500
        if self.location[-1][1]>500:self.location[-1][1]=0  
            



pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption(screenName)
clock=pygame.time.Clock()

keys = pygame.key.get_pressed()
s=snake()



running = True
while running:
    screen.fill("Black")
    s.switchScreen()
    s.move()
    s.print()

    pygame.display.update()


    clock.tick(framerate)


pygame.quit()

