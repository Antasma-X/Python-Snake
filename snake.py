import pygame
import config
import random

class Apple:
    score=0
    font=pygame.font.Font(None,50)
    scoreLabel=font.render(f"Score:{score}",True,"White")
    def __init__(self) -> None:
        self.surf=pygame.Surface(config.defaultSize)
        self.location=(60,60)
        self.rect=self.surf.get_rect(topleft=self.location)


    def showScore(screen):
        screen.blit(Apple.scoreLabel,(660,0))
        
    def spawn(self,s):
        
        while True:
            x=random.randrange(0,800,20)
            y=random.randrange(0,500,20)
            if len(list(filter(lambda a:(x,y)==a,s.location))):continue
            break
        return (x,y)
    
    def collide(self,screen,s):

        if self.rect.colliderect(s.headRect):
            Apple.score+=1
            self.location=self.spawn(s)            
            self.rect=self.surf.get_rect(topleft=self.location)
            Apple.scoreLabel=Apple.font.render(f"Score:{Apple.score}",True,"White")
            Apple.showScore(screen)

            s.snake.append(pygame.Surface(config.defaultSize))
            s.location.append([s.location[-1][0]+20*s.directionX,s.location[-1][1]+20*s.directionY])
    
    def print(self,screen):
        screen.blit(self.surf,self.location)
        self.surf.fill("Red")


class Snake:

    def __init__(self) -> None:
        self.snake= [pygame.Surface(config.defaultSize)]
        self.location=[config.defaultSnakeLocation]
        self.directionX=1
        self.directionY=0
        self.headRect=self.snake[-1].get_rect(topleft=(self.location[-1]))

    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:   
                if event.key==pygame.K_DOWN:
                    self.directionX=0
                    self.directionY=1
                elif event.key==pygame.K_UP:
                    self.directionX=0
                    self.directionY=-1
                elif event.key==pygame.K_RIGHT:
                    self.directionX=1
                    self.directionY=0
                elif event.key==pygame.K_LEFT:
                    self.directionX=-1
                    self.directionY=0
                

    def print(self,screen):
        temp=self.snake.pop(0)
        self.snake.append(temp)

        self.location.append([self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY])
        self.location.pop(0)

        self.headRect=self.snake[-1].get_rect(topleft=(self.location[-1]))

        for i in range(len(self.snake)):
            self.snake[i].fill('White')
            screen.blit(self.snake[i],tuple(self.location[i]))
    
    def switchScreen(self):
        if self.location[-1][0]<0:self.location[-1][0]=config.screenSize[0]
        if self.location[-1][0]>800:self.location[-1][0]=0
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
    


