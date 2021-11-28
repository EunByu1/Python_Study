from tkinter import *
import tkinter.font as font 
import subprocess
import pygame

# 배경음 
pygame.init()
pygame.mixer.music.load("C:\\Users\\82105\\Desktop\\GUI\\BG.mp3")
pygame.mixer.music.play(-1)


# GAME 선언 
def Memory_GAME():
    pygame.mixer.music.stop()
    subprocess.call("GAME1.py", shell=True)
    pygame.mixer.music.play(-1)

def Shooting_GAME():
    pygame.mixer.music.stop()
    subprocess.call("GAME2.py", shell=True)
    pygame.mixer.music.play(-1)

def Avoiding_GAME():
    pygame.mixer.music.stop()
    subprocess.call("GAME3.py", shell=True)
    pygame.mixer.music.play(-1)

def Ball_GAME():
    pygame.mixer.music.stop()
    subprocess.call("GAME4.py", shell=True)
    pygame.mixer.music.play(-1)

def RPG_GAME():
    pygame.mixer.music.stop()
    subprocess.call("GAME5.py", shell=True)
    pygame.mixer.music.play(-1)

# 창 설정 
window = Tk()
window.title("GAME_WORLD")
window.geometry("540x380+600+250")
window.resizable(False,False)
window['bg'] = '#000000'


# 창 Label 설정 
D1_Label = Label(window, text = "--------------------------------------------------------", bg = 'black', fg = '#5c7ee6', font=('Tahoma', 17, 'bold'))
D1_Label.place(x=0, y=8)

Title_Label = Label(window, text = "🎮 GAME WORLD 🎮", bg = 'black', fg = '#5c7ee6', font=('Tahoma', 32, 'bold'))
Title_Label.place(x=44, y=33)

D2_Label = Label(window, text = "--------------------------------------------------------", bg = 'black', fg = '#5c7ee6', font=('Tahoma', 17, 'bold'))
D2_Label.place(x=0, y=83)

D3_Label = Label(window, text = "--------------------------------------------------------", bg = 'black', fg = '#5c7ee6', font=('Tahoma', 17, 'bold'))
D3_Label.place(x=0, y=310)

D4_Label = Label(window, text = "🚗🚓🚕🛺🚙🚌🚐🚑🚒🚚🚜🚲🛴🛵🏍🏎🚄🚅🚃🚋🚂🚁🛥", bg = 'black', fg = '#5c7ee6', font=('Tahoma', 16))
D4_Label.place(x=0, y=340)


# 이미지 
photo1 = PhotoImage(file = "C:\\Users\\82105\\Desktop\\GUI\\SPACE_1.png")
IG_Label = Label(window, image=photo1, bg ='black')
IG_Label.place(x=20, y=209)

photo2 = PhotoImage(file = "C:\\Users\\82105\\Desktop\\GUI\\SPACE_1.png")
IG_Labe2 = Label(window, image=photo2, bg ='black')
IG_Labe2.place(x=436, y=209)


# text로 된 버튼 생성 
memory = Button(window, text="Memory_Game", width = 12, height = 1, padx = 5, pady = 5.5, fg = "black", bg = "white", font = ('Segeo UI Emoji',10), command = Memory_GAME)
memory.place(x=30, y = 148)

Shooting = Button(window, text="Shooting_Game", width = 12, height = 1, padx = 5, pady = 5.5, fg = "black", bg = "white", font = ('Segeo UI Emoji',10), command = Shooting_GAME)
Shooting.place(x= 210, y =148)

Avoiding = Button(window, text="Avoiding_Game", width = 12, height = 1, padx = 5, pady = 5.5, fg = "black", bg = "white", font = ('Segeo UI Emoji',10), command = Avoiding_GAME)
Avoiding.place(x=380, y=148)

Ball = Button(window, text="Ball_Game", padx = 5, width = 12, height = 1, pady = 5.5, fg = "black", bg = "white", font = ('Segeo UI Emoji',10), command = Ball_GAME)
Ball.place(x=123, y=220)

RPG  = Button(window, text="RPG_Game", padx = 5, width = 12, height = 1, pady = 5.5, fg = "black", bg = "white", font = ('Segeo UI Emoji',10), command=RPG_GAME)
RPG.place(x=300, y=220)
window.mainloop()