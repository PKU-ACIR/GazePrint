import pygame
import sys
import random
from multiprocessing import Process
import time
import os
from arc_demo_print_doubleblink import ARC

pygame.init()
h = pygame.font.get_fonts()
width = 10320
height = 1440
# width = 1536
# height = 864
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
x = 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
screen.fill((255, 255, 255))
pygame.display.set_caption('眼神打字')
myfont = pygame.font.Font(None, 100)
myfont2 = pygame.font.Font(None, 200)
font_name = pygame.font.match_font('fangsong')  # 2.获得字体文件
font = pygame.font.Font(font_name, 80)  # 1.获取font对象（需要字体文件）
black = 0, 0, 0
white = 255, 255, 255
textImage = myfont.render('Hello', True, black)
textImage2 = myfont.render('Please start calibration first', True, black)
textImage3 = myfont.render('Wait for the preparation', True, black)
textImage4 = myfont.render('Starting calibration  LOOK AT THE POINT', True, black)
textImage5 = myfont.render('calibration not started yet please wait,please move your head back and forth', True, black)
textImage6 = myfont.render('Start', True, black)
textImage7 = font.render('校准已完成！打字过程中会记录您的打字时长！字幕消失后即可开始打字', True, black)
textImage7plus = myfont.render('Then click to type', True, black)
textImage8 = myfont.render('Stare to type now', True, black)
# 绘制内容：text为内容，True为是否抗锯齿， WHITE是字体颜色
textImagetime = myfont.render('The time you use to press this letter:', True, black)
miaoshu=myfont.render('s', True, black)
font_surface = font.render('首先，我们会进行校准！在校准完成后可以开始打字：', True, black)  # 3.将文字生成 surface对象
font_surface2 = font.render('你需要通过注视锁定你要打的字，当眼神注视对应字幕的键盘时，键盘框会亮起；', True, black)  # 3.将文字生成 surface对象
font_surface3 = font.render('然后，你可以双眨眼确定打印该字母；双眨眼后字母会显示在屏幕上方。', True, black)  # 3.将文字生成 surface对象
font_surface3plus = font.render('键盘中有四个功能键，分别是：', True, black) 
font_surface4 = font.render('clear: 清除全部内容 '
                           'delete: 删除上一个字母 '
                           'quit: 退出打字游戏 '
                           'space: 空格键 ', True, black)  
font_surface5 = font.render('准备中...', True, black)
textImagetime = myfont.render('The total time you use to type:', True, black)  
Q = myfont2.render('Q', True, black)
W = myfont2.render('W', True, black)
E = myfont2.render('E', True, black)
R = myfont2.render('R', True, black)
T = myfont2.render('T', True, black)
Y = myfont2.render('Y', True, black)
U = myfont2.render('U', True, black)
I = myfont2.render('I', True, black)
O = myfont2.render('O', True, black)
P = myfont2.render('P', True, black)
A = myfont2.render('A', True, black)
S = myfont2.render('S', True, black)
D = myfont2.render('D', True, black)
F = myfont2.render('F', True, black)
G = myfont2.render('G', True, black)
H = myfont2.render('H', True, black)
J = myfont2.render('J', True, black)
K = myfont2.render('K', True, black)
L = myfont2.render('L', True, black)
Z = myfont2.render('Z', True, black)
X = myfont2.render('X', True, black)
C = myfont2.render('C', True, black)
V = myfont2.render('V', True, black)
B = myfont2.render('B', True, black)
N = myfont2.render('N', True, black)
M = myfont2.render('M', True, black)
quitkey = myfont.render('quit', True, black)
blank = myfont.render('space', True, black)
clearkey = myfont.render('clear', True, black)
deletekey = myfont.render('delete', True, black)


# 加载图片
def draw():
    pygame.draw.rect(screen, (255, 0, 5), (20, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (700, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (1380, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (2060, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (2740, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (20, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (700, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (1380, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (2060, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (2740, 730, 660, 560), 5)

    pygame.draw.rect(screen, (255, 0, 5), (3460, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (4140, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (4820, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (5500, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (6180, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (3460, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (4140, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (4820, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (5500, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (6180, 730, 660, 560), 5)

    pygame.draw.rect(screen, (255, 0, 5), (6900, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (7580, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (8260, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (8940, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (9620, 150, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (6900, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (7580, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (8260, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (8940, 730, 660, 560), 5)
    pygame.draw.rect(screen, (255, 0, 5), (9620, 730, 660, 560), 5)

    screen.blit(Q, (330, 400))
    screen.blit(W, (1010, 400))
    screen.blit(E, (1690, 400))
    screen.blit(R, (2370, 400))
    screen.blit(T, (3050, 400))

    screen.blit(X, (3770, 400))
    screen.blit(U, (4450, 400))
    screen.blit(I, (5130, 400))
    screen.blit(O, (5810, 400))
    screen.blit(P, (6490, 400))

    screen.blit(A, (7210, 400))
    screen.blit(C, (7890, 400))
    screen.blit(V, (8570, 400))
    screen.blit(blank, (9200, 400))
    screen.blit(deletekey, (9880, 400))

    screen.blit(F, (330, 1000))
    screen.blit(H, (1010, 1000))
    screen.blit(J, (1690, 1000))
    screen.blit(Y, (2370, 1000))
    screen.blit(L, (3050, 1000))

    screen.blit(G, (3770, 1000))
    screen.blit(Z, (4450, 1000))
    screen.blit(S, (5130, 1000))
    screen.blit(K, (5810, 1000))
    screen.blit(D, (6490, 1000))

    screen.blit(B, (7210, 1000))
    screen.blit(N, (7890, 1000))
    screen.blit(M, (8570, 1000))
    screen.blit(quitkey, (9200, 1000))
    screen.blit(clearkey, (9880, 1000))

success_time = time.time()
chenggongle=0
while True:
    screen.fill((white))
    screen.blit(font_surface, (3500,50))#4.将文字surface对象 放到背景surface上
    screen.blit(font_surface2, (3500, 200))#4.将文字surface对象 放到背景surface上
    screen.blit(font_surface3, (3500, 350))#4.将文字surface对象 放到背景surface上
    screen.blit(font_surface3plus, (3500, 500))#4.将文字surface对象 放到背景surface上
    screen.blit(font_surface4, (3500, 650))#4.将文字surface对象 放到背景surface上
    screen.blit(font_surface5, (3500, 800))#4.将文字surface对象 放到背景surface上
    pygame.display.update()
    t = ARC()
    while True:

        success, finished = t.calibration()
        if success:
            screen.fill((white))
            pygame.draw.circle(screen, 'green', (5160, 720), 30, width)
            screen.blit(textImage4, (5000, 800))
            pygame.display.update()
            print(finished)
            if finished:
                break
        else:
            screen.fill((white))
            pygame.draw.circle(screen, 'green', (5160, 720), 30, width)
            screen.blit(textImage5, (5000, 800))
            pygame.display.update()
        if (success and finished):
            break
    screen.fill((white))
    screen.blit(textImage7, (50, 50))
    draw()

    pygame.display.update()
    time.sleep(3)
 
    FIRE_EVENT = pygame.USEREVENT + 1  # This is just a integer.
    pygame.time.set_timer(FIRE_EVENT, 3000)  # 1000 milliseconds is 15 seconds.
    i = ""
    iold=""
    last_word=""
    before_word=""
    flag_openmouth=0
    a1=-1000
    a2=-1000
    totalcal= time.time()
    while True:

        for event in pygame.event.get():
            # 判断用户是否点了关闭按钮
            if event.type == pygame.KEYDOWN:
                # 卸载所有模块
                pygame.quit()
                # 终止程序
                sys.exit()
        ifquit = 0
        ifnot = 0
        i=iold
        before_word=last_word #用来记录上一次眼睛注视的是什么字母
        a1_before=a1
        a2_before=a2
        pos = t.calculate()
        if t.tracker.is_print ==1 and t.tracker.is_close==0:


            if pos[0] >= 20 and pos[0] <= 680 and pos[1] >= 150 and pos[1] <= 710:
                last_word='Q'
                text_lastword= myfont.render('Q', True, black)
                textImageword = myfont.render('Q', True, black)
                i = i + 'Q'
                out = myfont.render(i, True, black)
                a1 = 20
                a2 = 150

            elif pos[0] >= 700 and pos[0] <= 1360 and pos[1] >= 150 and pos[1] <= 710:
                last_word='W'
                text_lastword= myfont.render('W', True, black)
                i = i + 'W'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('W', True, black)
                a1 = 700
                a2 = 150

            elif pos[0] >= 1380 and pos[0] <= 2040 and pos[1] >= 150 and pos[1] <= 710:
                last_word='E'
                text_lastword= myfont.render('E', True, black)
                i = i + 'E'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('E', True, black)
                a1 = 1380
                a2 = 150
            elif pos[0] >= 2060 and pos[0] <= 2720 and pos[1] >= 150 and pos[1] <= 710:
                last_word='R'
                text_lastword= myfont.render('R', True, black)
                i = i + 'R'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('R', True, black)
                a1 = 2060
                a2 = 150
            elif pos[0] >= 2740 and pos[0] <= 3420 and pos[1] >= 150 and pos[1] <= 710:
                last_word='T'
                text_lastword= myfont.render('T', True, black)
                i = i + 'T'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('T', True, black)
                a1 = 2740
                a2 = 150
            elif pos[0] >= 3460 and pos[0] <= 3560 and pos[1] >= 150 and pos[1] <= 710:
                last_word='X'
                text_lastword= myfont.render('X', True, black)
                i = i + 'X'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('X', True, black)
                a1 = 3460
                a2 = 150
            elif pos[0] >= 3600 and pos[0] <= 4815 and pos[1] >= 150 and pos[1] <= 999:
                last_word='U'
                text_lastword= myfont.render('U', True, black)
                i = i + 'U'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('U', True, black)
                a1 = 4140
                a2 = 150
            elif pos[0] >= 4820 and pos[0] <= 5480 and pos[1] >= 150 and pos[1] <= 1000:
                last_word='I'
                text_lastword= myfont.render('I', True, black)
                i = i + 'I'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('I', True, black)
                a1 = 4820
                a2 = 150
            elif pos[0] >= 5500 and pos[0] <= 6160 and pos[1] >= 150 and pos[1] <= 1000:
                last_word='O'
                text_lastword= myfont.render('O', True, black)
                i = i + 'O'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('O', True, black)
                a1 = 5500
                a2 = 150
            elif pos[0] >= 6180 and pos[0] <= 6950 and pos[1] >= 150 and pos[1] <= 715:
                last_word='P'
                text_lastword= myfont.render('P', True, black)
                i = i + 'P'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('P', True, black)
                a1 = 6180
                a2 = 150
            elif pos[0] >= 6950 and pos[0] <= 7000 and pos[1] >= 150 and pos[1] <= 710:
                last_word='A'
                text_lastword= myfont.render('A', True, black)
                i = i + 'A'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('A', True, black)
                a1 = 6900
                a2 = 150
            elif pos[0] >= 7080 and pos[0] <= 7990 and pos[1] >= 150 and pos[1] <= 715:
                last_word='C'
                text_lastword= myfont.render('C', True, black)
                i = i + 'C'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('C', True, black)
                a1 = 7580
                a2 = 150
            elif pos[0] >= 8000 and pos[0] <= 8940 and pos[1] >= 150 and pos[1] <= 1000:
                last_word='V'
                text_lastword= myfont.render('V', True, black)
                i = i + 'V'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('V', True, black)
                a1 = 8260
                a2 = 150
            elif pos[0] >= 8945 and pos[0] <= 10000 and pos[1] >= 150 and pos[1] <= 710:
                last_word=' '
                text_lastword= myfont.render(' ', True, black)
                i = i + ' '
                out = myfont.render(i, True, black)
                textImageword = myfont.render(' ', True, black)
                a1 = 8940
                a2 = 150
            elif pos[0] >= 10000 and pos[0] <= 10300 and pos[1] >= 150 and pos[1] <= 710:
                last_word='delete'
                text_lastword= myfont.render('delete', True, black)
                i = i[:-1]
                out = myfont.render(i, True, black)
                textImageword = myfont.render('delete', True, black)
                a1 = 9620
                a2 = 150
            elif pos[0] >= 20 and pos[0] <= 680 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='F'
                text_lastword= myfont.render('F', True, black)
                i = i + 'F'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('F', True, black)
                a1 = 20
                a2 = 730
            elif pos[0] >= 700 and pos[0] <= 1360 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='H'
                text_lastword= myfont.render('H', True, black)
                i = i + 'H'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('H', True, black)
                a1 = 700
                a2 = 730
            elif pos[0] >= 1380 and pos[0] <= 1480 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='J'
                text_lastword= myfont.render('J', True, black)
                i = i + 'J'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('J', True, black)
                a1 = 1380
                a2 = 730
            elif pos[0] >= 1500 and pos[0] <= 2720 and pos[1] >= 725 and pos[1] <= 1290:
                last_word='Y'
                text_lastword= myfont.render('Y', True, black)
                i = i + 'Y'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('Y', True, black)
                a1 = 2060
                a2 = 730
            elif pos[0] >= 2740 and pos[0] <= 3420 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='L'
                text_lastword= myfont.render('L', True, black)
                i = i + 'L'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('L', True, black)
                a1 = 2740
                a2 = 730
            elif pos[0] >= 3460 and pos[0] <= 4120 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='G'
                text_lastword= myfont.render('G', True, black)
                i = i + 'G'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('G', True, black)
                a1 = 3460
                a2 = 730
            elif pos[0] >= 4140 and pos[0] <= 4800 and pos[1] >= 1000 and pos[1] <= 1290:
                last_word='Z'
                text_lastword= myfont.render('Z', True, black)
                i = i + 'Z'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('Z', True, black)
                a1 = 4140
                a2 = 730
            elif pos[0] >= 4820 and pos[0] <= 5480 and pos[1] >= 1000 and pos[1] <= 1290:
                last_word='S'
                text_lastword= myfont.render('S', True, black)
                i = i + 'S'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('S', True, black)
                a1 = 4820
                a2 = 730
            elif pos[0] >= 5500 and pos[0] <= 6160 and pos[1] >= 1000 and pos[1] <= 1290:
                last_word='K'
                text_lastword= myfont.render('K', True, black)
                i = i + 'K'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('K', True, black)
                a1 = 5500
                a2 = 730
            elif pos[0] >= 6180 and pos[0] <= 6900 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='D'
                text_lastword= myfont.render('D', True, black)
                i = i + 'D'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('D', True, black)
                a1 = 6180
                a2 = 730
            elif pos[0] >= 6910 and pos[0] <= 7560 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='B'
                text_lastword= myfont.render('B', True, black)
                i = i + 'B'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('B', True, black)
                a1=6900
                a2=730
            elif pos[0] >= 7580 and pos[0] <= 8240 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='N'
                text_lastword= myfont.render('N', True, black)
                i = i + 'N'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('N', True, black)
                a1 = 7580
                a2 = 730
            elif pos[0] >= 8260 and pos[0] <= 8920 and pos[1] >= 1050 and pos[1] <= 1290:
                last_word='M'
                text_lastword= myfont.render('M', True, black)
                i = i + 'M'
                out = myfont.render(i, True, black)
                textImageword = myfont.render('M', True, black)
                a1 = 8260
                a2 = 730
            elif pos[0] >= 8940 and pos[0] <= 9600 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='QUIT'
                text_lastword= myfont.render('QUIT', True, black)
                i = i
                out = myfont.render(i, True, black)
                textImageword = myfont.render('QUIT', True, black)
                ifquit = 1
                a1 = 8940
                a2 = 730
            elif pos[0] >= 9620 and pos[0] <= 10300 and pos[1] >= 730 and pos[1] <= 1290:
                last_word='CLEAR'
                text_lastword= myfont.render('CLEAR', True, black)
                i = ""
                out = myfont.render(i, True, black)
                textImageword = myfont.render('CLEAR', True, black)
                a1 = 9620
                a2 = 730
                

            else:
                textImageword = myfont.render('You are not staring at a letter', True, black)
                out = myfont.render(i, True, black)
                ifnot = 1

        screen.fill((white))
        #screen.blit(textImageword, (3500, 50))
        draw()
        guangbiao_iold =iold+'|'
        out = myfont.render(guangbiao_iold, True, black)
        screen.blit(out, (4000, 50))
        if(chenggongle): #只要打出了一个字母，就会把这个值设为1，从而显示时间
            timetotal = myfont.render(typetime, True, black)
            screen.blit(textImagetime, (50, 50))
            screen.blit(timetotal, (1200, 50))
        #pygame.draw.circle(screen, 'green', (pos[0], pos[1]), 30, width)
        if ifnot == 0:
            pygame.draw.rect(screen, [0, 255, 0], [a1, a2, 660, 560], 10)
        pygame.display.update()
        if(t.tracker.is_close==1 and ifnot==0):
            chenggongle=1
           # time2=time.process_time()-success_time
            success_time=time.time()
            screen.fill((white))
            draw()
            
            typetime=str(time.time()-totalcal)
            print("total_time", typetime)
            typetime+='s'
            timetotal = myfont.render(typetime, True, black)
            screen.blit(textImagetime, (50, 50))
            screen.blit(timetotal, (1200, 50))
               # screen.blit(textImageword, (3500, 50))
            if(before_word=="CLEAR"):
                i_last=""
            elif(before_word=="delete"):
                i_last = iold[:-1]
            elif(before_word=="QUIT"):
                ifquit=1
            else:
                i_last=iold+before_word
            guangbiao_i_last=i_last+"|"
            out = myfont.render(guangbiao_i_last, True, black)
            screen.blit(out, (4000, 50))
            pygame.draw.rect(screen, [255,0, 0], [a1_before, a2_before, 660, 560], 30)
            pygame.display.update()
            time.sleep(1)
            iold = i_last
            if (ifquit):
                    # 卸载所有模块
                pygame.quit()
                    # 终止程序
                sys.exit()




        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # 卸载所有模块
                pygame.quit()
                # 终止程序
                sys.exit()
            if  event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((white))
                draw()
                screen.blit(textImageword, (3500, 50))
                out = myfont.render(i, True, black)
                screen.blit(out, (4000, 50))
                pygame.display.update()
                iold =i
                if (ifquit):
                    # 卸载所有模块
                    pygame.quit()
                    # 终止程序
                    sys.exit()





















