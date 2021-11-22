# [0] 게임에 필요한 모듈을 import 
import random
import pygame
import sys
# [0.0] pygame의 기능들로부터 QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect을 import  
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect   



# [1] pygame의 화면과 키의 반복기능, 게임창에 적을 이름들을 표시 (작은 글씨와 큰 글씨 지정) 
pygame.init()  # pygame.init() : pygame의 모듈을 초기화 하는 코드로써, pygame을 시작할 때 초기화 시켜주는 역할을 함 
pygame.display.set_caption("♣ SHO_OT-GAME ♣")   # 콘솔 창 이름을 적는 코드 
pygame.key.set_repeat(15,15)
SURFACE = pygame.display.set_mode((1000,600))   # 콘솔 창의 크기 설정 
FPSCLOCK = pygame.time.Clock()                  # 프레임 저장 
Big_font = pygame.font.SysFont(None, 80)        # 폰트: 기본 , size: 80
Small_font = pygame.font.SysFont(None, 40)      # 폰트: 기본 , size: 40


# [2] 도형 설정
class Draw:
    def __init__(self,col,rect,speed = 0):
        self.col = col      # 색
        self.rect = rect    # 모양
        self.speed = speed  # 스피드 
    def move(self):         # 지정된 스피드만큼 도형 이동 
        self.rect.centerx += self.speed
    def draw_E(self):       # ellipse 메서드 : 타원 draw    
        pygame.draw.ellipse(SURFACE,self.col,self.rect)
    def draw_R(self):       # rect 메서드 : 사각형 draw
        pygame.draw.rect(SURFACE,self.col,self.rect)    # rect(화면, 색, (x, y, 가로길이, 세로길이), 굵기) / 굵기 설정 X = 꽉 찬 사각형 

# [3] 기본적인 게임틀 설정 
def Game_Border():
    Start_Point = [(100,150),(100,150),(100,550),(900,150)]
    End_Point = [(100,550),(900,150),(900,550),(900,550)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(243, 97, 166),Start_Point[index],End_Point[index]) 
        # line 메서드 : 선 draw / (화면, 색, 시작위치, 끝위치, 굵기)

def main():
# [4] 변수 선언부
    rock_speed = -5
    RockWIDTH = 50
    RockHEIGHT = 50
    xpos = 880
    ypos = random.randint(0,8)
    Rock = []
    game_start = False
    Miss = 0
    Score = 0
    Beam_Count = 0
    Cir = Draw((255, 255, 255), Rect(50,300, 30,30))
    Beam = Draw((255, 108, 235), Rect(Cir.rect.centerx, Cir.rect.centery, 5, 5), 10)

# [5] 메세지 출력 
    while True:
        message_Title = Big_font.render("SHO_OT-GAME", True, (255, 255, 255))                               # 게임제목 적기
        message_Score = Small_font.render("Score: {}".format(Score), True, (255, 255, 255))                # 스코어
        message_Miss = Small_font.render("Miss Point: {}".format(Miss), True, (255, 255, 255))             # 놓친장애물수
        message_game_start = Small_font.render("Game_start : Click the Space_bar", True, (241, 95, 95))  # 게임시작
        message_game_over = Big_font.render("Game_over_Score : {}".format(Score), True, (255, 178, 217))   # 게임오버
        message_caution = Small_font.render("Shoot Key: 'A' , Beam got faster : Keep pressing 'A' Key", True, (255, 255, 255))
        SURFACE.fill((0, 0, 0))             # 콘솔창 화면 색상 설정 

# [6] 이벤트 설정
        for event in pygame.event.get():    # 어떤 이벤트가 발생하였는지 검사 
            if event.type == QUIT:          # 창을 닫는 이벤트가 발생하였을 때 실행 
                pygame.quit()               # 게임 종료 
                sys.exit()
            elif event.type == KEYDOWN:     # 키를 누르는 이벤트가 발생하였을 때 실행
                if event.key == K_SPACE:    # 누른 키가 space_bar일 때 실행 
                    rock_speed = -5
                    Miss = 0
                    Score = 0
                    game_start = True
                elif event.key == K_UP:
                    Cir.rect.centery -= 10
                elif event.key == K_DOWN:
                    Cir.rect.centery += 10
                elif event.key == K_a:
                    if Beam_Count == 0:
                        Beam_Count =1
                        Beam.rect.center = Cir.rect.center
                    else:
                        Beam.draw_E()
                        Beam.move()     # Beam 속력 증가 
       
# [7] 게임이 실행되었을 때 설정        
        if  game_start:
            SURFACE.blit(message_Title, (290, 20))   # 화면상에 제목 표시
            SURFACE.blit(message_Score, (750, 160))  # 화면상에 스코어 표시
            SURFACE.blit(message_caution,(133,100))  # 화면상에 주의사항 표시
            SURFACE.blit(message_Miss,(700,200))     # 놓친블럭수 표시
            Game_Border()
            Cir.draw_E()

            if Cir.rect.centery <= 170:
                Cir.rect.centery = 170
            elif Cir.rect.centery >= 530:
                Cir.rect.centery = 530

# [8] 빔이 발사되고있을 때 설정 
            if Beam_Count == 1:
                Beam.draw_E()
                Beam.move()
                if Beam.rect.centerx >= 900:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0

# [9] 장애물의 출현
            if len(Rock) == 0:
                # 등장하는 장애물의 크기를 랜덤으로 바꾸어주고, Rock의 리스트에 추가 
                Rock.append(Draw((255, 185, 185), Rect(xpos, ypos * 40 + 170, RockWIDTH - ypos*3 , RockHEIGHT - ypos*3), rock_speed))
            elif len(Rock) ==1:
                # 한개의 리스트 항목 발생 시, 장애물 출발시킴  
                Rock[0].draw_R()
                Rock[0].move()
                if Rock[0].rect.colliderect(Beam.rect):
                    # 장애물과 빔이 만나면 실행 
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Score +=100         # 점수를 100점 올림 
                    rock_speed -=0.25   # 장애물의 속도를 증가시킴
                    del Rock[0]         # 다음블럭 생성을 위해 첫번째 리스트 항목 제거 
                    ypos = random.randint(0, 8)
                elif Rock[0].rect.centerx <= 100:
                    # 장애물과 빔이 만나지 못해, 장애물의 x좌표가 100이하이면 실행 
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Miss +=1
                    del Rock[0]
                    ypos = random.randint(0, 8)
            if Miss == 3:
                # Miss를 3번 하면 실행 
                game_start = False      # 게임 종료

# [10] game_start가 True가 아닌 상황들 
        elif not game_start and Miss ==3:
            SURFACE.blit(message_game_over, (100, 225))
            SURFACE.blit(message_game_start, (100, 310))
        else:
            SURFACE.blit(message_Title, (297, 230))
            SURFACE.blit(message_game_start, (283, 300))

        pygame.display.update()     # 작성한 코드를 콘솔 창에 표시해주는 코드임 (게임 화면 다시 그리기)
        FPSCLOCK.tick(30)           # 게임화면의 초당 프레임 수를 설정 
    

if __name__ == '__main__':          # 코드를 실행할 때마다 main()함수를 불러오도록 함 
    main()