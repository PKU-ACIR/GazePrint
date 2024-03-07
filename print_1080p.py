import pygame
import sys
import random
from multiprocessing import Process
import time
import os
from arc_demo_1080p import ARC

pygame.init()
h = pygame.font.get_fonts()
width = 1920
height = 1080
# width = 1536
# height = 864
# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
x = 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
screen.fill((255, 255, 255))
pygame.display.set_caption('眼神打字')
myfont = pygame.font.Font(None, 40)
myfont2 = pygame.font.Font(None, 40)
font_name = pygame.font.match_font('fangsong')  # 2.获得字体文件
font = pygame.font.Font(font_name, 40)  # 1.获取font对象（需要字体文件）
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
textImage9 = font.render('请在3s内眨眼一下', True, black)
# 绘制内容：text为内容，True为是否抗锯齿， WHITE是字体颜色
textImagetime = myfont.render('The time you use to press this letter:', True, black)
miaoshu = myfont.render('s', True, black)
font_surface = font.render('首先，我们会进行校准！校准时不要眨眼或者闭眼：', True, black)  # 3.将文字生成 surface对象
font_surface2 = font.render('你需要通过注视锁定你要打的字，当眼神注视对应字幕的键盘时，键盘框会亮起；', True,
                            black)  # 3.将文字生成 surface对象
font_surface3 = font.render('然后，你可以双眨眼确定打印该字母；双眨眼后字母会显示在屏幕上方。', True,
                            black)  # 3.将文字生成 surface对象
font_surface3plus = font.render('键盘中有三个功能键，分别是：', True, black)
font_surface4 = font.render('clear: 清除全部内容 '
                            'delete: 删除上一个字母 '
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
dot = myfont2.render('.', True, black)
Z = myfont2.render('Z', True, black)
X = myfont2.render('X', True, black)
C = myfont2.render('C', True, black)
V = myfont2.render('V', True, black)
B = myfont2.render('B', True, black)
N = myfont2.render('N', True, black)
M = myfont2.render('M', True, black)


blank = myfont.render('space', True, black)
clearkey = myfont.render('clear', True, black)
deletekey = myfont.render('delete', True, black)
quitkey = myfont.render('quit', True, black)
bug=1

# 绘制键盘
def draw():
    pygame.draw.rect(screen, (0, 0, 0), (5, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (190, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0,0,0), (375, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0,0,0), (560, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (745, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (930, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1115, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1300, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1485, 90, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1670, 90, 180, 320), 5)

    pygame.draw.rect(screen, (0, 0, 0), (5, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (190, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (375, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (560, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (745, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (930, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1115, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1300, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1485, 420, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1670, 420, 180, 320), 5)

    pygame.draw.rect(screen, (0, 0, 0), (5, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (190, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (375, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (560, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (745, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (930, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1115, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1300, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1485, 750, 180, 320), 5)
    pygame.draw.rect(screen, (0, 0, 0), (1670, 750, 180, 320), 5)


    screen.blit(Q, (90, 230))
    screen.blit(W, (275, 230))
    screen.blit(E, (460, 230))
    screen.blit(R, (645, 230))
    screen.blit(T, (830, 230))

    screen.blit(Y, (1015, 230))
    screen.blit(U, (1200, 230))
    screen.blit(I, (1385, 230))
    screen.blit(O, (1570, 230))
    screen.blit(P, (1755, 230))

    screen.blit(A, (90, 560))
    screen.blit(S, (275, 560))
    screen.blit(D, (450, 560))
    screen.blit(F, (645, 560))
    screen.blit(G, (830, 560))

    screen.blit(H, (1015, 560))
    screen.blit(J, (1200, 560))
    screen.blit(K, (1385, 560))
    screen.blit(L, (1570, 560))
    screen.blit(dot, (1755, 560))

    screen.blit(Z, (90, 890))
    screen.blit(X, (275, 890))
    screen.blit(C, (450, 890))
    screen.blit(V, (645, 890))
    screen.blit(B, (830, 890))

    screen.blit(N, (1015, 890))
    screen.blit(M, (1200, 890))
    screen.blit(blank, (1385, 890))
    screen.blit(deletekey, (1570, 890))
    screen.blit(clearkey, (1755, 890))


# 只要打出了一个字母，就会把successprintaword这个值设为1，从而显示时间
successprintaword = 0

while True:
    screen.fill((white))
    # 打印眼神打字的说明内容
    screen.blit(font_surface, (10, 50))
    screen.blit(font_surface2, (10, 150))
    screen.blit(font_surface3, (10, 250))
    screen.blit(font_surface3plus, (10, 350))
    screen.blit(font_surface4, (10, 450))
    screen.blit(font_surface5, (10, 600))
    pygame.display.update()
    t = ARC()
    # 校准，采用的是中心单点校准
    while True:

        success, finished = t.calibration()
       
        if success:
            screen.fill((white))
            pygame.draw.circle(screen, 'green', (width/2, height/2), 15, width)
            screen.blit(textImage4, (width/2-50, height/2+100))
            if bug :
                earnow=str(round(t.tracker.blink_detector.ear,3))
                if t.tracker.blink_detector.ear>t.tracker.blink_detector.thres1: # normal, green
                    earpri=myfont.render(earnow, True, (0,255,0))
                elif t.tracker.blink_detector.ear<t.tracker.blink_detector.thres2: # closed, red
                    earpri=myfont.render(earnow, True, (255,0,0))
                else: # blinking, orange
                    earpri=myfont.render(earnow, True, (255,128,0))
                screen.blit(earpri, (800, 10))
            pygame.display.update()
            print(finished)
            
            if finished:
                break
        else:
            screen.fill((white))
            pygame.draw.circle(screen, 'green', (width/2, height/2), 15 , width)
            screen.blit(textImage5, (width/2-200, height/2+100))
            if bug :
                earnow=str(round(t.tracker.blink_detector.ear,3))
                if t.tracker.blink_detector.ear>t.tracker.blink_detector.thres1: # normal, green
                    earpri=myfont.render(earnow, True, (0,255,0))
                elif t.tracker.blink_detector.ear<t.tracker.blink_detector.thres2: # closed, red
                    earpri=myfont.render(earnow, True, (255,0,0))
                else: # blinking, orange
                    earpri=myfont.render(earnow, True, (255,128,0))
                screen.blit(earpri, (800, 10))
            pygame.display.update()
        if (success and finished):
            break
    clock1=time.time()
    screen.fill(white)
    pygame.display.update()
    while True:

        success = t.calibration2()
       
        screen.blit(textImage9, (width/2-50, height/2+100))
        if bug :
            earnow=str(round(t.tracker.blink_detector.ear,3))
               
            screen.blit(earpri, (800, 10))
            pygame.display.update()
        clock2=time.time()-clock1
        if clock2>3:
                break
    screen.fill((white))
    screen.blit(textImage7, (50, 50))
    draw()
    pygame.display.update()
    time.sleep(3)
    # FIRE_EVENT = pygame.USEREVENT + 1  # This is just a integer.
    # pygame.time.set_timer(FIRE_EVENT, 3000)  # 1000 milliseconds is 15 seconds.
    # 初始化设置
    # i , i_old, gaze_word, before_word 都初始化为空
    # a1,a2 分别表示此次注视的键盘左上角坐标位置，这样只需要加上键盘的长和款就可以高亮显示
    # time_startprint 表示开始打字的时间
    i = ""
    iold = ""
    gaze_word = ""
    before_word = ""
    a1 = -1000
    a2 = -1000
    time_startprint = time.time()

    # 下面进入打字循环，除非停止打字，否则一直在该循环中
    while True:

        for event in pygame.event.get():
            # 判断用户是否点了关闭按钮
            if event.type == pygame.KEYDOWN:
                # 卸载所有模块
                pygame.quit()
                # 终止程序
                sys.exit()
        # ifquit 表示是否触发quit键;
        # ifnot 表示此时没有注视任何一个键盘
        # iold 表示上一次打字结束后的总句子，在每一次开始打字前我们要把i同步为和上次打字结束的iold相同的句子
        # 用before_word=gaze_word来记录上一次眼镜注视的字母
        # gaze_word 事实上就是每一次判断pos的视线落点后对应的那个字母
        # 同时用a1_before,a2_before来记录上一次的a1,a2;
        ifquit = 0
        ifnot = 0
        before_word = gaze_word
        a1_before = a1
        a2_before = a2

        pos = t.calculate()

        # 注意，pos计算视线落点后，对应的： gaze_word为当前注视字母；text_gazeword为gaze_word的pygame打印
        # a1，a2 更新为当前注视键盘左上角坐标
        #只有在不眨眼的时候才能识别注视位置，否则就用之前识别的结果，也就是不再更新before_word了
        if t.tracker.is_print == 1 and t.tracker.is_doubleblink == 0:
            if pos[0] <= 185 and pos[1] <= 410:
                gaze_word = 'Q'
                text_gazeword = myfont.render('Q', True, black)
                a1 = 5
                a2 = 90
            elif pos[0] >= 190 and pos[0] <= 370 and pos[1] <= 410:
                gaze_word = 'W'
                text_gazeword = myfont.render('W', True, black)
                a1 = 190
                a2 = 90

            elif pos[0] >= 375 and pos[0] <= 555 and pos[1] <= 410:
                gaze_word = 'E'
                text_gazeword = myfont.render('E', True, black)
                a1 = 375
                a2 = 90
            elif pos[0] >= 560 and pos[0] <= 740 and pos[1] <= 410:
                gaze_word = 'R'
                text_gazeword = myfont.render('R', True, black)
                a1 = 560
                a2 = 90
            elif pos[0] >= 745 and pos[0] <= 925 and pos[1] <= 410:
                gaze_word = 'T'
                text_gazeword = myfont.render('T', True, black)
                a1 = 745
                a2 = 90
            elif pos[0] >= 930 and pos[0] <= 1110 and pos[1] <= 410:
                gaze_word = 'Y'
                text_gazeword = myfont.render('Y', True, black)
                a1 = 930
                a2 = 90
            elif pos[0] >= 1115 and pos[0] <= 1295 and pos[1] <= 410:
                gaze_word = 'U'
                text_gazeword = myfont.render('U', True, black)
                a1 = 1115
                a2 = 90
            elif pos[0] >= 1300 and pos[0] <= 1480 and pos[1] <= 410:
                gaze_word = 'I'
                text_gazeword = myfont.render('I', True, black)
                a1 = 1300
                a2 = 90
            elif pos[0] >= 1485 and pos[0] <= 1665 and pos[1] <= 410:
                gaze_word = 'O'
                text_gazeword = myfont.render('O', True, black)
                a1 = 1485
                a2 = 90
            elif pos[0] >= 1670 and pos[1] <= 410:
                gaze_word = 'P'
                text_gazeword = myfont.render('P', True, black)
                a1 = 1670
                a2 = 90
            elif  pos[0] <= 185 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'A'
                text_gazeword = myfont.render('A', True, black)
                a1 = 5
                a2 = 420
            elif pos[0] >= 190 and pos[0] <= 370 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'S'
                text_gazeword = myfont.render('S', True, black)
                a1 = 190
                a2 = 420
            elif pos[0] >= 375 and pos[0] <= 555 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'D'
                text_gazeword = myfont.render('D', True, black)
                a1 = 375
                a2 = 420
            elif pos[0] >= 560 and pos[0] <= 740 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'F'
                text_gazeword = myfont.render('F', True, black)
                a1 = 560
                a2 = 420
            elif pos[0] >= 745 and pos[0] <= 925  and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'G'
                text_gazeword = myfont.render('G', True, black)
                a1 = 745
                a2 = 420
            elif pos[0] >= 930 and pos[0] <= 1110 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'H'
                text_gazeword = myfont.render('H', True, black)
                a1 = 930
                a2 = 420
            elif pos[0] >= 1115 and pos[0] <= 1295 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'J'
                text_gazeword = myfont.render('J', True, black)
                a1 = 1115
                a2 = 420
            elif pos[0] >= 1300 and pos[0] <= 1480 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'K'
                text_gazeword = myfont.render('K', True, black)
                a1 = 1300
                a2 = 420
            elif pos[0] >= 1485 and pos[0] <= 1665 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = 'L'
                text_gazeword = myfont.render('L', True, black)
                a1 = 1485
                a2 = 420
            elif pos[0] >= 1670 and pos[1] >= 420 and pos[1] <= 740:
                gaze_word = '.'
                text_gazeword = myfont.render('.', True, black)
                a1 = 1670
                a2 = 420
            elif pos[0] <= 185 and pos[0] <= 4800 and pos[1] >= 750:
                gaze_word = 'Z'
                text_gazeword = myfont.render('Z', True, black)
                a1 = 5
                a2 = 750
            elif pos[0] >= 190 and pos[0] <= 370 and pos[1] >= 750:
                gaze_word = 'X'
                text_gazeword = myfont.render('X', True, black)
                a1 = 190
                a2 = 750
            elif pos[0] >= 375 and pos[0] <= 555 and pos[1] >= 750:
                gaze_word = 'C'
                text_gazeword = myfont.render('C', True, black)
                a1 = 374
                a2 = 750
            elif pos[0] >= 560 and pos[0] <= 740 and pos[1] >= 750:
                gaze_word = 'V'
                text_gazeword = myfont.render('V', True, black)
                a1 = 560
                a2 = 750
            elif pos[0] >= 745 and pos[0] <= 925 and pos[1] >= 750:
                gaze_word = 'B'
                text_gazeword = myfont.render('B', True, black)
                a1 = 745
                a2 = 750
            elif pos[0] >= 930 and pos[0] <= 1110 and pos[1] >= 750:
                gaze_word = 'N'
                text_gazeword = myfont.render('N', True, black)
                a1 = 930
                a2 = 750
            elif pos[0] >= 1115 and pos[0] <= 1295 and pos[1] >= 750:
                gaze_word = 'M'
                text_gazeword = myfont.render('M', True, black)
                a1 = 1115
                a2 = 750
            elif pos[0] >= 1300 and pos[0] <= 1480 and pos[1] >= 750:
                gaze_word = ' '
                text_gazeword = myfont.render(' ', True, black)
                a1 = 1300
                a2 = 750
            elif pos[0] >= 1485 and pos[0] <= 1665 and pos[1] >= 750:
                gaze_word = 'delete'
                text_gazeword = myfont.render('delete', True, black)
                i = i[:-1]
                out = myfont.render(i, True, black)
                a1 = 1485
                a2 = 750
            elif pos[0] >= 1670 and pos[1] >= 750:
                gaze_word = 'CLEAR'
                text_gazeword = myfont.render('CLEAR', True, black)
                out = myfont.render(i, True, black)
                a1 = 1670
                a2 =750

            else:
                text_gazeword = myfont.render('You are not staring at a letter', True, black)
                out = myfont.render(i, True, black)
                ifnot = 1

        screen.fill((white))
        draw()
        if bug :
            earnow=str(round(t.tracker.blink_detector.ear,3))+'    '+str(round(t.tracker.blink_detector.thres1,3))+'    '+str(round(t.tracker.blink_detector.thres2,3))
            if t.tracker.blink_detector.ear>t.tracker.blink_detector.thres1: # normal, green
                earpri=myfont.render(earnow, True, (0,255,0))
            elif t.tracker.blink_detector.ear<t.tracker.blink_detector.thres2: # closed, red
                earpri=myfont.render(earnow, True, (255,0,0))
            else: # blinking, orange
                earpri=myfont.render(earnow, True, (255,128,0))
            screen.blit(earpri, (800, 10))


        # guangbiao_iold表示上一次的句子加上光标，方便打字人知道现在打字结果，有多少空格等；把光标结果显示在右上方
        guangbiao_iold = iold + '|'

        # 下面为每一次无论是否张嘴打字都要显示的内容：现在打出来的句子加上光标，打完现有内容的时间和当前注视键盘。
        out = myfont.render(guangbiao_iold, True, black)
        screen.blit(out, (400, 10))
        # 只要打出了一个字母，就会把successprintaword这个值设为1，从而显示时间
        if (successprintaword):
            timetotal = myfont.render(typetime, True, black)
            screen.blit(timetotal, (10, 10))
        # ifnot = 0 ，当前的确在注视键盘，那么把键盘变绿
        if ifnot == 0:
            pygame.draw.rect(screen, [0, 255, 0], [a1, a2, 180, 320], 10)
        pygame.display.update()

        # 下面判断是否要打新的字母：
        # 触发打字的条件：t.tracker.is_doubleblink == 1

        if (t.tracker.is_doubleblink == 1 and ifnot == 0):
            successprintaword = 1
            screen.fill((white))
            draw()
            typetime = str(time.time() - time_startprint)
            typetime += 's'
            timetotal = myfont.render(typetime, True, black)
            screen.blit(timetotal, (10, 10))
            # 为什么用的都是before_word 而不是gaze_word:
            # 因为在触发打字的时候，我们不想要现在的注视结果，而想要眨眼前一刻注视的结果，而每次识别前before_word都会更新为gaze_word。
            # i_last表示打完这个字后的打字结果；guangbiao_i_last再加上光标；
            if (before_word == "CLEAR"):
                i_last = ""
            elif (before_word == "delete"):
                i_last = iold[:-1]
            elif (before_word == "QUIT"):
                ifquit = 1
            else:
                i_last = iold + before_word
            guangbiao_i_last = i_last + "|"
            # 将out更新为打完字后的并显示内容：新句子和变红的键盘（表示成功打字），注意此时变色的是a1_before
            out = myfont.render(guangbiao_i_last, True, black)
            screen.blit(out, (400, 10))
            pygame.draw.rect(screen, [255, 0, 0], [a1_before, a2_before, 180, 320], 10)
            pygame.display.update()
            time.sleep(1)
            # 把i_old更新为新句子
            iold = i_last

            if (ifquit):
                # 卸载所有模块
                pygame.quit()
                # 终止程序
                sys.exit()

# 每一次进入while循环的打字，屏幕上显示的是上一次完成的内容。
# 计算好pos后，画键盘，显示无论是否触发都要显示的时间等信息；
# 判断是否触发，如果触发，更新内容，刷新页面。
