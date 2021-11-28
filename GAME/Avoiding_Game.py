import random
import math
import time as Time
import pygame
import sys
from pygame.locals import QUIT,Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE

class Total:
    def __init__(self,col,rect,speed = 0): #col:채우는색, rect:그리는 직사각형(위치,크기), speed(이동속도,공만),dir(이동방향, 공만)
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-85, 85) +200

    def move(self):#공을 움직인다 , radians를 사용해서 dir을 라디안으로 변환, X축과Y축의 방향성분구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
    def draw(self):
        pygame.draw.ellipse(WINDOW, self.col, self.rect)

pygame.init()
pygame.display.set_caption("♠ Avoiding_Game ♠")
pygame.key.set_repeat(15,15)
WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
Bg_Sound_1 = pygame.mixer.Sound("C:\\Users\\82105\\Desktop\\GUI\\GAME3_1.mp3")
Bg_Sound_2 = pygame.mixer.music.load("C:\\Users\\82105\\Desktop\\GUI\\GAME3_2.mp3")
Bg_Sound_1.play(-1)
FPSCLOCK = pygame.time.Clock()


def main():
    # 게임 진행과 메세지
    game_start = False
    game_over = False
    tmp = 0
 
    time = 0
    Font_Big    = pygame.font.SysFont(None, 60)
    Font_Middle = pygame.font.SysFont(None, 45)
    Font_Small  = pygame.font.SysFont(None, 33)
    Message_Start = Font_Big.render("GAME_START : Click the SpaceBar", True, (163,243,255))
    Message_Over  = Font_Big.render("[ GAME_OVER ]", True, (163,243,255))
    Message_Add   = Font_Small.render("End = Press any key", True, (224, 54, 16))


    # player Circle
    Circle_x = 400
    Circle_y = 400
    Circle = Total((255, 255, 255), Rect(Circle_x, Circle_y, 10, 10))

    # Obstacle
    Ball_x = []
    Ball_y = []
    B_one = []  # i의 반복되는 만큼 1이 저장된다.
    B_point = []  # i가 반복되는 값을 저장한다
    B_velocity = []  # 공 하나당의 속도를 담는다
    for i in range(1,80):
        i *= 10
        B_point.append(i)
        B_one.append(1)
        B_velocity.append(random.randint(2,10))

    while True:
        Message_Time = Font_Middle.render("time : %.2f s" %time, True, (255, 255, 255))
        if game_start == True:
            time += 0.035 #시간을 측정 
        if game_over == True:
            game_start = False
        WINDOW.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT or tmp == 1:
                if tmp == 1:
                    Time.sleep(0.1)
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Circle.rect.centerx -= 15
                if event.key == K_RIGHT:
                    Circle.rect.centerx += 15
                if event.key == K_UP:
                    Circle.rect.centery -= 15
                if event.key == K_DOWN:
                    Circle.rect.centery += 15
                if event.key == K_SPACE:
                    game_start = True
                    game_over = False
                    time = 0
                    Ball_x = []
                    Ball_y = []
                    Bg_Sound_1.stop()
                    pygame.mixer.music.play(-1,2)

        if game_start == False:
            if game_over == True:
                WINDOW.blit(Message_Over, (250, 320))     # 250,300으로 위치 설정 
                WINDOW.blit(Message_Add, (300, 370))
                WINDOW.blit(Message_Time,  (320, 423))      # 310,393으로 위치 설정 
                tmp = 1
                Time.sleep(0.3)
            else:
                WINDOW.blit(Message_Start, (50, 350))     # 180,350으로 위치 설정 
                WINDOW.blit(Message_Time, (312, 430))      # 320,430으로 위치 설정 
        else:
            Circle.draw()
            if Circle.rect.centerx > 795:
                Circle.rect.centerx = 795
            elif Circle.rect.centerx < 5:
                Circle.rect.centerx = 5
            if Circle.rect.centery > 795:
                Circle.rect.centery = 795
            elif Circle.rect.centery < 5:
                Circle.rect.centery = 5
            for i in range(len(B_point)):
                Ball_x.append(Total((5, 250, 42), Rect(B_point[i], B_one[i], 2, 2),B_velocity[i]))
                Ball_y.append(Total((5, 250, 42), Rect(B_one[i], B_point[i], 2, 2),B_velocity[i]))
                Ball_x[i].draw()
                Ball_y[i].draw()
                if Ball_x[i].rect.centery < 1000:
                    Ball_x[i].move()
                if Ball_y[i].rect.centery < 1000:
                    Ball_y[i].move()

                if Ball_x[i].rect.centery < 0 or Ball_x[i].rect.centery >800:
                    Ball_x[i].dir = - Ball_x[i].dir
                elif Ball_x[i].rect.centerx < 0 or Ball_x[i].rect.centerx >800:
                    Ball_x[i].dir = 180 - Ball_x[i].dir
                if Ball_y[i].rect.centery < 0 or Ball_y[i].rect.centery > 800:
                    Ball_y[i].dir = - Ball_y[i].dir
                elif Ball_y[i].rect.centerx < 0 or Ball_y[i].rect.centerx > 800:
                    Ball_y[i].dir = 180 - Ball_y[i].dir

                if Circle.rect.colliderect(Ball_x[i].rect) or Circle.rect.colliderect(Ball_y[i].rect):
                    game_over = True
                    pygame.mixer.music.stop()
        
        pygame.display.update()
        FPSCLOCK.tick(28)

if __name__ == "__main__":
    main()