import pygame
import config
class apple:
    score=0
    def __init__(self) -> None:
        self.location=0

    def spawn(self):
        pass
        
class Snake:

    def __init__(self) -> None:
        self.snake= [pygame.Surface(config.defaultSize)]
        self.location=[config.defaultSnakeLocation]
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
                    self.snake.append(pygame.Surface(config.defaultSize))
                    self.location.append([self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY])

    def print(self,screen):
        temp=self.snake.pop(0)
        self.snake.append(temp)

        self.location.append([self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY])
        self.location.pop(0)

        for i in range(len(self.snake)):
            self.snake[i].fill('White')
            screen.blit(self.snake[i],tuple(self.location[i]))
    
    def switchScreen(self):
        if self.location[-1][0]<0:self.location[-1][0]=config.screenSize[0]
        if self.location[-1][0]>750:self.location[-1][0]=0
        if self.location[-1][1]<0:self.location[-1][1]=config.screenSize[1]
        if self.location[-1][1]>500:self.location[-1][1]=0  
            
    def death(self):
        for i in range(len(self.location)):
            for j in range(len(self.location)):
                if i==j:
                    continue
                if self.location[i]==self.location[j]:
                    pygame.quit()
                    exit()
    


