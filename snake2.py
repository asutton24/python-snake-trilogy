import pygame
from pygame import *
import random
global snake
global food
global dir

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def equals(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def reformat(self):
        z = [self.x , self.y]
        return z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, z):
        self.x=z

    def setY(self,z):
        self.y=z
def main():
    score = 0
    snake = [Point(318,360),Point(319,360), Point(320, 360)]
    food = Point(960, 360)
    pygame.init()
    screen = pygame.display.set_mode([1280, 720])
    running = True
    head = Point(320,360)
    direct = 3
    tick=0
    clock = pygame.time.Clock()
    random.seed()
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        temp = food.reformat()
        pygame.draw.rect(screen,(255,0,0),(temp[0],temp[1],1,1))
        for i in snake:
            temp = i.reformat()
            pygame.draw.rect(screen,(0,255,0),(temp[0],temp[1],1,1))
        pygame.display.update()
        clock.tick(120)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            if direct != 2:
                direct = 1
        elif pressed_keys[K_s]:
            if direct != 1:
                direct = 2
        elif pressed_keys[K_a]:
            if direct != 3:
                direct = 4
        elif pressed_keys[K_d]:
            if direct != 4:
                direct = 3
        if (direct == 1):
            snake.append(Point(head.getX(),head.getY()-1))
            head.setY(head.getY()-1)
        elif (direct == 2):
            snake.append(Point(head.getX(),head.getY()+1))
            head.setY(head.getY()+1)
        elif (direct == 3):
            snake.append(Point(head.getX()+1,head.getY()))
            head.setX(head.getX()+1)
        elif (direct == 4):
            snake.append(Point(head.getX()-1,head.getY()))
            head.setX(head.getX()-1)
        if (head.equals(food)):
            score+=1
            same = True
            while same:
                found = False
                p1 = random.randint(0,1279)
                p2 = random.randint(0,719)
                food = Point(p1,p2)
                for i in snake:
                    if food.equals(i):
                        found = True
                        break
                if not found:
                    same = False
            print(str(p1)+" "+str(p2))
        else :
            snake.remove(snake[0])
        if head.getX()<0 or head.getX()>1279 or head.getY()<0 or head.getY()>719:
            running = False
        for i in range(len(snake)-1):
            if head.equals(snake[i]):
                running = False

        pygame.time.delay(1)


    print(score)
    pygame.quit()

main()





