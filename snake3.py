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
        z = [self.x * 20, self.y * 20]
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
    score2 = 0
    win = 0
    snake = [Point(7,9),Point(8,9), Point(9, 9)]
    food = Point(14, 14)
    snake2 = [Point(21,19),Point(20,19),Point(19,19)]
    pygame.init()
    screen = pygame.display.set_mode([600, 600])
    running = True
    head = Point(9,9)
    head2 = Point(19,19)
    direct = 3
    direct2 = 4
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
        pygame.draw.rect(screen,(255,0,0),(temp[0],temp[1],20,20))
        for i in snake:
            temp = i.reformat()
            pygame.draw.rect(screen,(0,255,0),(temp[0],temp[1],20,20))
        for i in snake2:
            temp = i.reformat()
            pygame.draw.rect(screen,(0,0,255),(temp[0],temp[1],20,20))
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
        if pressed_keys[K_UP]:
            if direct2 != 2:
                direct2 = 1
        elif pressed_keys[K_DOWN]:
            if direct2 != 1:
                direct2 = 2
        elif pressed_keys[K_LEFT]:
            if direct2 != 3:
                direct2 = 4
        elif pressed_keys[K_RIGHT]:
            if direct2 != 4:
                direct2 = 3
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
        if (direct2 == 1):
            snake2.append(Point(head2.getX(),head2.getY()-1))
            head2.setY(head2.getY()-1)
        elif (direct2 == 2):
            snake2.append(Point(head2.getX(),head2.getY()+1))
            head2.setY(head2.getY()+1)
        elif (direct2 == 3):
            snake2.append(Point(head2.getX()+1,head2.getY()))
            head2.setX(head2.getX()+1)
        elif (direct2 == 4):
            snake2.append(Point(head2.getX()-1,head2.getY()))
            head2.setX(head2.getX()-1)
        if (head.equals(food)):
            score+=1
            same = True
            while same:
                found = False
                p1 = random.randint(0,29)
                p2 = random.randint(0,29)
                food = Point(p1,p2)
                for i in snake:
                    if food.equals(i):
                        found = True
                        break
                for i in snake2:
                    if food.equals(i):
                        found = True
                        break
                if not found:
                    same = False
        else :
            snake.remove(snake[0])
        if (head2.equals(food)):
            score2+=1
            same = True
            while same:
                found = False
                p1 = random.randint(0,29)
                p2 = random.randint(0,29)
                food = Point(p1,p2)
                for i in snake:
                    if food.equals(i):
                        found = True
                        break
                for i in snake2:
                    if food.equals(i):
                        found = True
                        break
                if not found:
                    same = False
        else :
            snake2.remove(snake2[0])
        if head.getX()<0 or head.getX()>29 or head.getY()<0 or head.getY()>29:
            running = False
            win = 2
        if head2.getX()<0 or head2.getX()>29 or head2.getY()<0 or head2.getY()>29:
            running = False
            win = 1
        for i in range(len(snake)-1):
            if head.equals(snake[i]):
                running = False
                win = 2
        for i in range(len(snake2)-1):
            if head2.equals(snake2[i]):
                running = False
                win = 1
        for i in range(len(snake2)-1):
            if head.equals(snake2[i]):
                running = False
                win = 2
        for i in range(len(snake)-1):
            if head2.equals(snake[i]):
                running = False
                win = 1
        if head.equals(head2):
            if score>score2:
                win = 1
            elif score==score2:
                win = 3
            else:
                win = 2
            running = False
        for i in range(50):
            pygame.time.delay(2)
            pressed_keys = pygame.key.get_pressed()


    if win == 1:
        print('Player 1 wins\nMikey loses')
    elif win == 2:
        print('Player 2 wins\nMikey loses')
    else:
        print('Tie')
    print('Scores:\nPlayer 1: '+str(score)+'\nPlayer 2: '+str(score2))
    pygame.quit()

main()