import pygame
from config import *
import snake
import random

class apple:
    def __init__(self) -> None:
        self.location=(400,400)

    def spawn(self):
        pass
        
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
                if event.key==pygame.K_BACKSPACE:
                    self.snake.append(pygame.Surface((20,20)))
                    self.location.append([self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY])

    def print(self):
        temp=self.snake.pop(0)
        self.snake.append(temp)

        self.location.append([self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY])
        self.location.pop(0)

        for i in range(len(self.snake)):
            self.snake[i].fill('White')
            screen.blit(self.snake[i],tuple(self.location[i]))
    
    def switchScreen(self):
        if self.location[-1][0]<0:self.location[-1][0]=750
        if self.location[-1][0]>750:self.location[-1][0]=0
        if self.location[-1][1]<0:self.location[-1][1]=500
        if self.location[-1][1]>500:self.location[-1][1]=0  
            
    def death(self):
        for i in range(len(self.location)):
            for j in range(len(self.location)):
                if i==j:
                    continue
                if self.location[i]==self.location[j]:
                    pygame.quit()
                    exit()
    
    def score(self):
        pass






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
    s.death()
    pygame.display.update()


    clock.tick(framerate)


pygame.quit()

