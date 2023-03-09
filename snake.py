import pygame
pygame.init()
keys = pygame.key.get_pressed()

class body:
    def __init__(self) -> None:
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
            if keys[pygame.K_UP]:
                self.directionX=0
                self.directionY=-1
                
            if keys[pygame.K_DOWN]:
                self.directionX=0
                self.directionY=1
                
            if keys[pygame.K_RIGHT]:
                self.directionX=1
                self.directionY=0

            if keys[pygame.K_LEFT]:
                self.directionX=-1
                self.directionY=0

    def print(self):
        temp=self.snake.pop(0)
        self.snake.append(temp)

        self.location.append((self.location[-1][0]+20*self.directionX,self.location[-1][1]+20*self.directionY))
        self.location.pop(0)

        for i in range(len(self.snake)):
            self.snake[i].fill='White'
            screen.blit(self.snake[i],self.location[i])


    



