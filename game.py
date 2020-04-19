#!/usr/bin/env python

import pygame,sys,random,math,shelve
from pygame.locals import *

class card():
    def __init__(self,player,type,value):
        self.player = player
        self.type = type
        self.value = value

def mx(p,color):
    m = 0
    for i in range(len(p)):
        if p[i].type == color and p[i].value > m:
            m = p[i].value
    return m

def mn(p,a):
    m = 15
    for i in range(len(p)):
        if p[i].value < m and p[i].value > a:
            m = p[i].value
    return m

def refresh(screen,p1,p2,p3,p4,dealt,deck,trump,w):
    screen.fill(green)
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(650,530,200,40))
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('New Game', True, win1, (0,255,0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 550)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(650,470,200,40))
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Next deal', True, win1, (0,255,0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 490)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    if len(dealt) == 4 or len(dealt) == 0:
        pygame.draw.rect(DISPLAYSURF,(0,255,0),(1300,100,200,40))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Save Game', True, win1, (0,255,0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1400, 120)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(DISPLAYSURF,(0,255,0),(1300,150,200,40))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Load Game', True, win1, (0,255,0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1400, 170)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    for i in range(len(p4)):
        a = 'gray_back.png'
        #a = str(p4[i].value)+p4[i].type+'.png'
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(80,140))
        DISPLAYSURF.blit(img,(400+50*i,800))
    for i in range(len(p1)):
        a = 'blue_back.png'
        #a = str(p1[i].value) + p1[i].type + '.png'
        img = pygame.image.load(a)
        img = pygame.transform.rotate(img,90)
        img = pygame.transform.scale(img,(140,80))
        DISPLAYSURF.blit(img,(100,200+50*i))
    for i in range(len(p2)):
        a = 'green_back.png'
        #a = str(p2[i].value) + p2[i].type + '.png'
        img = pygame.image.load(a)
        img = pygame.transform.scale(img,(80,140))
        DISPLAYSURF.blit(img,(400 + 50*i,100))
    for i in range(len(p3)):
        a = 'purple_back.png'
        #a = str(p3[i].value) + p3[i].type + '.png'
        img = pygame.image.load(a)
        img = pygame.transform.rotate(img,270)
        img = pygame.transform.scale(img,(140,80))
        DISPLAYSURF.blit(img,(1400,200+50*i))
    for i in range(len(dealt)):
        if dealt[i].player == 1:
            a = str(dealt[i].value) + dealt[i].type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(80,140))
            DISPLAYSURF.blit(img,(450,500))
        if dealt[i].player == 2:
            a = str(dealt[i].value) + dealt[i].type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(80,140))
            DISPLAYSURF.blit(img,(700,250))
        if dealt[i].player == 3:
            a = str(dealt[i].value) + dealt[i].type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(80,140))
            DISPLAYSURF.blit(img,(900,500))
        if dealt[i].player == 4:
            a = str(dealt[i].value) + dealt[i].type + '.png'
            img = pygame.image.load(a)
            img = pygame.transform.scale(img,(80,140))
            DISPLAYSURF.blit(img,(700,600))
    a = '14' + trump + '.png'
    img = pygame.image.load(a)
    img = pygame.transform.scale(img,(80,140))
    DISPLAYSURF.blit(img,(100,0))
    for i in range(w[0]):
        img = pygame.image.load('blue_back.png')
        img = pygame.transform.scale(img,(30,50))
        DISPLAYSURF.blit(img,(100+20*i,820))
    for i in range(w[1]):
        img = pygame.image.load('green_back.png')
        img = pygame.transform.scale(img,(30,50))
        DISPLAYSURF.blit(img,(450+20*i,40))
    for i in range(w[2]):
        img = pygame.image.load('purple_back.png')
        img = pygame.transform.scale(img,(30,50))
        DISPLAYSURF.blit(img,(1300+20*i,820))
    for i in range(w[3]):
        img = pygame.image.load('gray_back.png')
        img = pygame.transform.scale(img,(30,50))
        DISPLAYSURF.blit(img,(450+20*i,950))
    pygame.display.update()

def get_cards(check,p,deck,k):
    arr = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
    arr2 = ['H','C','S','D']
    if(len(check) == 0):
        num1 = random.randint(0,12)
        num2 = random.randint(0,3)
        a = arr[num1]+arr2[num2]
        check.append(a)
        deck.append(card(k,arr2[num2],num1+2))
        p.append(card(k,arr2[num2],num1+2))
        return a
    else:
        num1 = random.randint(0,12)
        num2 = random.randint(0,3)
        b = arr[num1] + arr2[num2]
        c = card(k,arr2[num2],num1+2)
        for i in range(len(check)):
            if check[i] == b:
                b = get_cards(check,p,deck,k)
        check.append(b)
        deck.append(card(k,arr2[num2],num1+2))
        p.append(card(k,arr2[num2],num1+2))
        return b;

def get_trump(p):
    q = [0,0,0,0]
    for i in range(len(p)):
        if p[i].type == 'H':
            q[0] = q[0] + 1
        if p[i].type == 'D':
            q[1] = q[1] + 1
        if p[i].type == 'S':
            q[2] = q[2] + 1
        if p[i].type == 'C':
            q[3] = q[3] + 1
    max = q[0]
    j = 0
    for i in range(len(q)):
        if q[i] > max:
            max = q[i]
            j = i
    if j == 0:
        return 'H'
    elif j == 1:
        return 'D'
    elif j == 2:
        return 'S'
    else:
        return 'C'

def arrange(p,dealt,deck,trump,w):
    h = []
    d = []
    s = []
    c = []
    for i in range(len(p)):
        if p[i].type == 'H':
            h.append(p[i])
        elif p[i].type == 'S':
            s.append(p[i])
        elif p[i].type == 'D':
            d.append(p[i])
        else:
            c.append(p[i])
    p = []
    for i in range(len(h)):
        p.append(h[i])
    for i in range(len(s)):
        p.append(s[i])
    for i in range(len(d)):
        p.append(d[i])
    for i in range(len(c)):
        p.append(c[i])
    return p

def start(screen,p1,p2,p3,p4,deck,dealt,trump,w,win):
    check = []
    arr = ['H','D','S','C']
    for j in range(4):
        for i in range(13):
            a = (i+2,arr[j])
            check.append(a)
    random.shuffle(check)
    i = 0
    for i in range(52):
        a = check[i]
        if i<13:
            p1.append(card(1,a[1],a[0]))
        elif i<26:
            p2.append(card(2,a[1],a[0]))
        elif i<39:
            p3.append(card(3,a[1],a[0]))
        else:
            p4.append(card(4,a[1],a[0]))
        deck.append(card(0,a[1],a[0]))
    if win == 1:
        a = get_trump(p1)
    elif win == 2:
        a = get_trump(p2)
    elif win == 3:
        a = get_trump(p3)
    else:
        a = get_trump(p4)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,a,w)
    return a

def play_user(screen,p1,p2,p3,p4,dealt,deck,trump,w,a):
    first = 0
    if a == 1:
        p = p1
    elif a == 2:
        p = p2
    elif a == 3:
        p = p3
    else:
        p = p4
    k = 0
    l = []
    f = []
    r = []
    while True:
        just = pygame.mouse.get_pos()
        if just[0] > 100 and just[0] < 240 and just[1] > 200 and just[1] < 280 + 50*len(p) and first == 1 and a == 1:
            for i in range(len(p)):
                c = str(p[i].value)+p[i].type+'.png'
                img = pygame.image.load(c)
                img = pygame.transform.rotate(img,90)
                img = pygame.transform.scale(img,(140,80))
                DISPLAYSURF.blit(img,(100,200+50*i))
        elif just[0] > 400 and just[0] < 480 + 50*len(p) and just[1] > 100 and just[1] < 240 and first == 1 and a == 2:
            for i in range(len(p)):
                c = str(p[i].value)+p[i].type+'.png'
                img = pygame.image.load(c)
                img = pygame.transform.scale(img,(80,140))
                DISPLAYSURF.blit(img,(400+50*i,100))
        elif just[0] > 1400 and just[0] < 1540 and just[1] > 200 and just[1] < 280 + 50*len(p) and first == 1 and a == 3:
            for i in range(len(p)):
                c = str(p[i].value)+p[i].type+'.png'
                img = pygame.image.load(c)
                img = pygame.transform.rotate(img,90)
                img = pygame.transform.scale(img,(140,80))
                DISPLAYSURF.blit(img,(1400,200+50*i))
        elif just[0] > 400 and just[0] < 480 + 50*len(p) and just[1] > 800 and just[1] < 940 and first == 1 and a == 4:
            for i in range(len(p)):
                c = str(p[i].value)+p[i].type+'.png'
                img = pygame.image.load(c)
                img = pygame.transform.scale(img,(80,140))
                DISPLAYSURF.blit(img,(400+50*i,800))
        else:
            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        pygame.display.update()
        first = 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                for i in range(len(p)):
                    c = str(p[i].value)+p[i].type+'.png'
                    img = pygame.image.load(c)
                    if a == 1:
                        img = pygame.transform.rotate(img,90)
                        img = pygame.transform.scale(img,(140,80))
                        DISPLAYSURF.blit(img,(100,200+50*i))
                    elif a == 2:
                        img = pygame.transform.scale(img,(80,140))
                        DISPLAYSURF.blit(img,(400+50*i,100))
                    elif a == 3:
                        img = pygame.transform.rotate(img,90)
                        img = pygame.transform.scale(img,(140,80))
                        DISPLAYSURF.blit(img,(1400,200+50*i))
                    else:
                        img = pygame.transform.scale(img,(80,140))
                        DISPLAYSURF.blit(img,(400+50*i,800))
                pygame.display.update()
            if event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                    k = 2
                    return 1
                    break
                if a == 1:
                    y = int(math.floor((mouse[0]-100)/140))
                    x = math.floor((mouse[1]-200)/50)
                    x = int(x)
                elif a == 2:
                    x = math.floor((mouse[0]-400)/50)
                    y = math.floor((mouse[1]-100)/140)
                    x = int(x)
                    y = int(y)
                elif a == 3:
                    x = math.floor((mouse[1]-200)/50)
                    y = math.floor((mouse[0]-1400)/140)
                    x = int(x)
                    y = int(y)
                else:
                    x = math.floor((mouse[0] - 400)/50)
                    y = math.floor((mouse[1] - 800)/140)
                    y = int(y)
                    x = int(x)
                if x > -1 and x < len(p) and y == 0:
                    if len(dealt) == 0:
                        dealt.append(p[x])
                        p.pop(x)
                        if a == 1:
                            p1 = p
                        elif a == 2:
                            p2 = p
                        elif a == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        k = 1
                        break
                    else:
                        color = dealt[0].type
                        for i in range(len(p)):
                            if p[i].type == color:
                                l.append(p[i])
                            elif p[i].type == trump:
                                f.append(p[i])
                            else:
                                r.append(p[i])
                        if p[x].type == color:
                            dealt.append(p[x])
                            p.pop(x)
                            if a == 1:
                                p1 = p
                            elif a == 2:
                                p2 = p
                            elif a == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            k = 1
                            break
                        elif p[x].type != color and len(l) == 0:
                            dealt.append(p[x])
                            p.pop(x)
                            if a == 1:
                                p1 = p
                            elif a == 2:
                                p2 = p
                            elif a == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            k = 1
                            break
        if k == 1:
            break
    if k == 2:
        return 1
    else:
        return 0

def play_comp(screen,p1,p2,p3,p4,dealt,deck,trump,w,t):
    hm = mx(deck,'H')
    sm = mx(deck,'S')
    cm = mx(deck,'C')
    dm = mx(deck,'D')
    if t == 1:
        p = p1
    elif t == 2:
        p = p2
    elif t == 3:
        p = p3
    else:
        p = p4
    phm = mx(p,'H')
    pdm = mx(p,'D')
    psm = mx(p,'S')
    pcm = mx(p,'C')
    k = mn(p,0)
    if phm == 0:
        phm = 1
    if pdm == 0:
        pdm = 1
    if psm == 0:
        psm = 1
    if pcm == 0:
        pcm = 1
    a = []
    b = []
    for i in range(len(p)):
        if p[i].type == trump:
            a.append(p[i])
        else:
            b.append(p[i])
    if len(dealt) == 0:
        if phm == hm:
            for i in range(len(p)):
                if p[i].type == 'H' and p[i].value == hm:
                    dealt.append(p[i])
                    p.pop(i)
                    if t == 1:
                        p1 = p
                    elif t == 2:
                        p2 = p
                    elif t == 3:
                        p3 = p
                    else:
                        p4 = p
                    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    return
        elif pdm == dm:
            for i in range(len(p)):
                if p[i].type == 'D' and p[i].value == dm:
                    dealt.append(p[i])
                    p.pop(i)
                    if t == 1:
                        p1 = p
                    elif t == 2:
                        p2 = p
                    elif t == 3:
                        p3 = p
                    else:
                        p4 = p
                    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    return
        elif psm == sm:
            for i in range(len(p)):
                if p[i].type == 'S' and p[i].value == sm:
                    dealt.append(p[i])
                    p.pop(i)
                    if t == 1:
                        p1 = p
                    elif t == 2:
                        p2 = p
                    elif t == 3:
                        p3 = p
                    else:
                        p4 = p
                    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    return
        elif pcm == cm:
            for i in range(len(p)):
                if p[i].type == 'C' and p[i].value == cm:
                    dealt.append(p[i])
                    p.pop(i)
                    if t == 1:
                        p1 = p
                    elif t == 2:
                        p2 = p
                    elif t == 3:
                        p3 = p
                    else:
                        p4 = p
                    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    return
        else:
            k = mn(p,0)
            for i in range(len(p)):
                if p[i].value == k:
                    dealt.append(p[i])
                    p.pop(i)
                    if t == 1:
                        p1 = p
                    elif t == 2:
                        p2 = p
                    elif t == 3:
                        p3 = p
                    else:
                        p4 = p
                    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    return
    elif len(dealt) == 1 or len(dealt) == 2:
        color = dealt[0].type
        l = []
        r = []
        f = []
        max = mx(deck,color)
        for i in range(len(p)):
            if p[i].type == color:
                l.append(p[i])
            if p[i].type == trump:
                f.append(p[i])
            if p[i].type != color and p[i].type != trump:
                r.append(p[i])
        if len(l) == 0:
            if len(r) == 0:
                r = f
            if len(f) == 0:
                k = mn(p,0)
                for i in range(len(p)):
                    if p[i].value == k:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
            elif len(dealt) == 1:
                j = mn(f,0)
                for i in range(len(p)):
                    if p[i].value == j and p[i].type == trump:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
            elif len(dealt) == 2:
                if dealt[1].type == trump:
                    if mx(f,trump) > dealt[1].value:
                        j = mn(f,dealt[1].value)
                        for i in range(len(p)):
                            if p[i].value == j and p[i].type == trump:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                    else:
                        k = mn(r,0)
                        for i in range(len(p)):
                            if p[i].value == k:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                else:
                    if dealt[0].value == max:
                        k = mn(r,0)
                        for i in range(len(p)):
                            if p[i].value == k:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                    else:
                        k = mn(f,0)
                        for i in range(len(p)):
                            if p[i].value == k:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
        else:
            j = mx(l,color)
            k = mx(deck,color)
            if j == k:
                for i in range(len(p)):
                    if p[i].value == k and p[i].type == color:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
            else:
                for i in range(len(p)):
                    if p[i].value == mn(l,0) and p[i].type == color:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
    elif len(dealt) == 3:
        color = dealt[0].type
        l = []
        f = []
        r = []
        for i in range(len(p)):
            if p[i].type == color:
                l.append(p[i])
            if p[i].type == trump:
                f.append(p[i])
            if p[i].type!= color and p[i].type != trump:
                r.append(p[i])
        if len(l) == 0:
            if len(r) == 0:
                r = f
            if len(f) == 0:
                k = mn(r,0)
                for i in range(len(p)):
                    if p[i].value == k:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
            else:
                if dealt[2].type == trump:
                    if mx(f,trump) > dealt[2].value:
                        for i in range(len(p)):
                            if p[i].value == mn(f,dealt[2].value) and p[i].type == trump:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                    else:
                        for i in range(len(p)):
                            if p[i].value == mn(r,0):
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                elif dealt[1].type == trump:
                    for i in range(len(p)):
                        if p[i].value == mn(r,0):
                            dealt.append(p[i])
                            p.pop(i)
                            if t == 1:
                                p1 = p
                            elif t == 2:
                                p2 = p
                            elif t == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            return
                else:
                    if dealt[1].value == mx(deck,color) and dealt[1].type == color:
                        k = mn(r,0)
                        for i in range(len(p)):
                            if p[i].value == k:
                                dealt.append(p[i])
                                p.pop(i)
                                if t == 1:
                                    p1 = p
                                elif t == 2:
                                    p2 = p
                                elif t == 3:
                                    p3 = p
                                else:
                                    p4 = p
                                refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                                return
                    for i in range(len(p)):
                        if p[i].value == mn(f,0) and p[i].type == trump:
                            dealt.append(p[i])
                            p.pop(i)
                            if t == 1:
                                p1 = p
                            elif t == 2:
                                p2 = p
                            elif t == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            return
        else:
            j = mx(l,color)
            k = mx(dealt,color)
            for q in range(len(dealt)):
                if dealt[q].type == trump:
                    for i in range(len(p)):
                        if p[i].value == mn(l,0) and p[i].type == color:
                            dealt.append(p[i])
                            p.pop(i)
                            if t == 1:
                                p1 = p
                            elif t == 2:
                                p2 = p
                            elif t == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            return
            if dealt[1].value == k and dealt[1].type == color:
                for i in range(len(p)):
                    if p[i].value == mn(l,0) and p[i].type == color:
                        dealt.append(p[i])
                        p.pop(i)
                        if t == 1:
                            p1 = p
                        elif t == 2:
                            p2 = p
                        elif t == 3:
                            p3 = p
                        else:
                            p4 = p
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                        return
            else:
                if j > k:
                    for i in range(len(p)):
                        if p[i].value == j and p[i].type == color:
                            dealt.append(p[i])
                            p.pop(i)
                            if t == 1:
                                p1 = p
                            elif t == 2:
                                p2 = p
                            elif t == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            return
                else:
                    for i in range(len(p)):
                        if p[i].value == mn(l,0) and p[i].type == color:
                            dealt.append(p[i])
                            p.pop(i)
                            if t == 1:
                                p1 = p
                            elif t == 2:
                                p2 = p
                            elif t == 3:
                                p3 = p
                            else:
                                p4 = p
                            refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                            return

def get_winner(dealt,deck,trump):
    color = dealt[0].type
    for i in range(len(dealt)):
        for j in range(len(deck)):
            if deck[j].value == dealt[i].value and deck[j].type == dealt[i].type:
                deck.pop(j);
                break
    for i in range(len(dealt)):
        if dealt[i].type == trump:
            j = mx(dealt,trump)
            for k in range(len(dealt)):
                if dealt[k].type == trump and dealt[k].value == j:
                    return dealt[k].player
    j = mx(dealt,color)
    for i in range(len(dealt)):
        if dealt[i].value == j and dealt[i].type == color:
            return dealt[i].player

def game_1p(screen,win,save):
    dealt = []
    deck = []
    a = win
    chance = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    w = [0,0,0,0]
    l = 0
    trump = ''
    if save == 0:
        trump = start(DISPLAYSURF,p1,p2,p3,p4,deck,dealt,trump,w,win)
    p1 = arrange(p1,dealt,deck,trump,w)
    p2 = arrange(p2,dealt,deck,trump,w)
    p3 = arrange(p3,dealt,deck,trump,w)
    p4 = arrange(p4,dealt,deck,trump,w)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
    for i in range(13):
        l = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                        return 0
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 470 and mouse[1] < 510:
                        l = 1
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 150 and mouse[1] < 190:
                        print('Hello')
                        shelf = shelve.open('1p')
                        p1 = shelf['p1']
                        p2 = shelf['p2']
                        p3 = shelf['p3']
                        p4 = shelf['p4']
                        dealt = shelf['dealt']
                        deck = shelf['deck']
                        trump = shelf['trump']
                        w = shelf['w']
                        a = shelf['a']
                        win = shelf['win']
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 100 and mouse[1] < 140:
                        shelf = shelve.open('1p')
                        shelf['p1'] = p1
                        shelf['p2'] = p2
                        shelf['p3'] = p3
                        shelf['p4'] = p4
                        shelf['dealt'] = dealt
                        shelf['deck'] = deck
                        shelf['trump'] = trump
                        shelf['w'] = w
                        shelf['win'] = win
                        shelf['a'] = a
                        shelf.close()
                        print('Hi')
            if l == 1:
                break
        if win == 1:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            pygame.time.delay(1000)
        elif win == 2:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            pygame.time.delay(1000)
        elif win == 3:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            pygame.time.delay(1000)
        else:
            q = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            pygame.time.delay(1000)
        win = get_winner(dealt,deck,trump)
        w[win-1] = w[win-1] + 1
        dealt = []
        if q == 1:
            return 0
        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        if w[0] + w[2] == 7:
            DISPLAYSURF.fill(win1)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 1 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a
            elif a == 2 or a == 4:
                return (a+1)%4
        elif w[1] + w[3] == 7:
            DISPLAYSURF.fill(win2)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 2 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a+1
            elif a == 2 or a == 4:
                return a

def game_4p(screen,win,save):
    dealt = []
    deck = []
    a = win
    chance = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    w = [0,0,0,0]
    trump = ''
    if save == 0:
        trump = start(DISPLAYSURF,p1,p2,p3,p4,deck,dealt,trump,w,win)
    p1 = arrange(p1,dealt,deck,trump,w)
    p2 = arrange(p2,dealt,deck,trump,w)
    p3 = arrange(p3,dealt,deck,trump,w)
    p4 = arrange(p4,dealt,deck,trump,w)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
    for i in range(13):
        l = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                        return 0
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 470 and mouse[1] < 510:
                        l = 1
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 150 and mouse[1] < 190:
                        print('Hello')
                        shelf = shelve.open('4p')
                        p1 = shelf['p1']
                        p2 = shelf['p2']
                        p3 = shelf['p3']
                        p4 = shelf['p4']
                        dealt = shelf['dealt']
                        deck = shelf['deck']
                        trump = shelf['trump']
                        w = shelf['w']
                        a = shelf['a']
                        win = shelf['win']
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 100 and mouse[1] < 140:
                        shelf = shelve.open('4p')
                        shelf['p1'] = p1
                        shelf['p2'] = p2
                        shelf['p3'] = p3
                        shelf['p4'] = p4
                        shelf['dealt'] = dealt
                        shelf['deck'] = deck
                        shelf['trump'] = trump
                        shelf['w'] = w
                        shelf['win'] = win
                        shelf['a'] = a
                        shelf.close()
                        print('Hi')
            if l == 1:
                break
        if win == 1:
            q1 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            if q1 == 1:
                return 0
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            pygame.time.delay(1000)
        elif win == 2:
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            q1 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            if q1 == 1:
                return 0
            pygame.time.delay(1000)
        elif win == 3:
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            q1 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            if q1 == 1:
                return 0
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            pygame.time.delay(1000)
        else:
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            q1 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            if q1 == 1:
                return 0
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            pygame.time.delay(1000)
        if q1 == 1 or q2 == 1 or q3 == 1 or q4 == 1:
            return 0
        win = get_winner(dealt,deck,trump)
        w[win-1] = w[win-1] + 1
        dealt = []
        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        if w[0] + w[2] == 7:
            DISPLAYSURF.fill(win1)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 1 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a
            elif a == 2 or a == 4:
                return (a+1)%4
        elif w[1] + w[3] == 7:
            DISPLAYSURF.fill(win2)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 2 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a+1
            elif a == 2 or a == 4:
                return a

def game_3p(screen,win,save):
    dealt = []
    deck = []
    a = win
    chance = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    w = [0,0,0,0]
    trump = ''
    if save == 0:
        trump = start(DISPLAYSURF,p1,p2,p3,p4,deck,dealt,trump,w,win)
    p1 = arrange(p1,dealt,deck,trump,w)
    p2 = arrange(p2,dealt,deck,trump,w)
    p3 = arrange(p3,dealt,deck,trump,w)
    p4 = arrange(p4,dealt,deck,trump,w)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
    for i in range(13):
        l = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                        return 0
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 470 and mouse[1] < 510:
                        l = 1
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 150 and mouse[1] < 190:
                        print('Hello')
                        shelf = shelve.open('3p')
                        p1 = shelf['p1']
                        p2 = shelf['p2']
                        p3 = shelf['p3']
                        p4 = shelf['p4']
                        dealt = shelf['dealt']
                        deck = shelf['deck']
                        trump = shelf['trump']
                        w = shelf['w']
                        a = shelf['a']
                        win = shelf['win']
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 100 and mouse[1] < 140:
                        shelf = shelve.open('3p')
                        shelf['p1'] = p1
                        shelf['p2'] = p2
                        shelf['p3'] = p3
                        shelf['p4'] = p4
                        shelf['dealt'] = dealt
                        shelf['deck'] = deck
                        shelf['trump'] = trump
                        shelf['w'] = w
                        shelf['win'] = win
                        shelf['a'] = a
                        shelf.close()
                        print('Hi')
            if l == 1:
                break
        if win == 1:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            pygame.time.delay(1000)
        elif win == 2:
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            pygame.time.delay(1000)
        elif win == 3:
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            pygame.time.delay(1000)
        else:
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            pygame.time.delay(1000)
        if q2 == 1 or q3 == 1 or q4 == 1:
            return 0
        win = get_winner(dealt,deck,trump)
        w[win-1] = w[win-1] + 1
        dealt = []
        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        if w[0] + w[2] == 7:
            DISPLAYSURF.fill(win1)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 1 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a
            elif a == 2 or a == 4:
                return (a+1)%4
        elif w[1] + w[3] == 7:
            DISPLAYSURF.fill(win2)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 2 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a+1
            elif a == 2 or a == 4:
                return a

def game_2p_team(screen,win,save):
    dealt = []
    deck = []
    a = win
    chance = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    w = [0,0,0,0]
    trump = ''
    if save == 0:
        trump = start(DISPLAYSURF,p1,p2,p3,p4,deck,dealt,trump,w,win)
    p1 = arrange(p1,dealt,deck,trump,w)
    p2 = arrange(p2,dealt,deck,trump,w)
    p3 = arrange(p3,dealt,deck,trump,w)
    p4 = arrange(p4,dealt,deck,trump,w)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
    for i in range(13):
        l = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                        return 0
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 470 and mouse[1] < 510:
                        l = 1
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 150 and mouse[1] < 190:
                        print('Hello')
                        shelf = shelve.open('2p_team')
                        p1 = shelf['p1']
                        p2 = shelf['p2']
                        p3 = shelf['p3']
                        p4 = shelf['p4']
                        dealt = shelf['dealt']
                        deck = shelf['deck']
                        trump = shelf['trump']
                        w = shelf['w']
                        a = shelf['a']
                        win = shelf['win']
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 100 and mouse[1] < 140:
                        shelf = shelve.open('2p_team')
                        shelf['p1'] = p1
                        shelf['p2'] = p2
                        shelf['p3'] = p3
                        shelf['p4'] = p4
                        shelf['dealt'] = dealt
                        shelf['deck'] = deck
                        shelf['trump'] = trump
                        shelf['w'] = w
                        shelf['win'] = win
                        shelf['a'] = a
                        shelf.close()
                        print('Hi')
            if l == 1:
                break
        if win == 1:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            pygame.time.delay(1000)
        elif win == 2:
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            pygame.time.delay(1000)
        elif win == 3:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            pygame.time.delay(1000)
        else:
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            q2 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            if q2 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            pygame.time.delay(1000)
        if q2 == 1 or q4 == 1:
            return 0
        win = get_winner(dealt,deck,trump)
        w[win-1] = w[win-1] + 1
        dealt = []
        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        if w[0] + w[2] == 7:
            DISPLAYSURF.fill(win1)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 1 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a
            elif a == 2 or a == 4:
                return (a+1)%4
        elif w[1] + w[3] == 7:
            DISPLAYSURF.fill(win2)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 2 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a+1
            elif a == 2 or a == 4:
                return a

def game_2p_rival(screen,win,save):
    dealt = []
    deck = []
    a = win
    chance = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    w = [0,0,0,0]
    trump = ''
    if save == 0:
        trump = start(DISPLAYSURF,p1,p2,p3,p4,deck,dealt,trump,w,win)
    p1 = arrange(p1,dealt,deck,trump,w)
    p2 = arrange(p2,dealt,deck,trump,w)
    p3 = arrange(p3,dealt,deck,trump,w)
    p4 = arrange(p4,dealt,deck,trump,w)
    refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
    for i in range(13):
        l = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 530 and mouse[1] < 570:
                        return 0
                    if mouse[0] > 650 and mouse[0] < 850 and mouse[1] > 470 and mouse[1] < 510:
                        l = 1
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 150 and mouse[1] < 190:
                        print('Hello')
                        shelf = shelve.open('2p_rival')
                        p1 = shelf['p1']
                        p2 = shelf['p2']
                        p3 = shelf['p3']
                        p4 = shelf['p4']
                        dealt = shelf['dealt']
                        deck = shelf['deck']
                        trump = shelf['trump']
                        w = shelf['w']
                        a = shelf['a']
                        win = shelf['win']
                        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
                    if mouse[0] > 1300 and mouse[0] < 1500 and mouse[1] > 100 and mouse[1] < 140:
                        shelf = shelve.open('2p_rival')
                        shelf['p1'] = p1
                        shelf['p2'] = p2
                        shelf['p3'] = p3
                        shelf['p4'] = p4
                        shelf['dealt'] = dealt
                        shelf['deck'] = deck
                        shelf['trump'] = trump
                        shelf['w'] = w
                        shelf['win'] = win
                        shelf['a'] = a
                        shelf.close()
                        print('Hi')
            if l == 1:
                break
        if win == 1:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            pygame.time.delay(1000)
        elif win == 2:
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            pygame.time.delay(1000)
        elif win == 3:
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            pygame.time.delay(1000)
        else:
            q4 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,4)
            if q4 == 1:
                return 0
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,1)
            play_comp(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,2)
            q3 = play_user(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w,3)
            if q3 == 1:
                return 0
            pygame.time.delay(1000)
        if q3 == 1 or q4 == 1:
            return 0
        win = get_winner(dealt,deck,trump)
        w[win-1] = w[win-1] + 1
        dealt = []
        refresh(DISPLAYSURF,p1,p2,p3,p4,dealt,deck,trump,w)
        if w[0] + w[2] == 7:
            DISPLAYSURF.fill(win1)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 1 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a
            elif a == 2 or a == 4:
                return (a+1)%4
        elif w[1] + w[3] == 7:
            DISPLAYSURF.fill(win2)
            fontObj = pygame.font.Font('freesansbold.ttf', 64)
            textSurfaceObj = fontObj.render('Team 2 wins', True, win1, green)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (850, 450)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            if a == 1 or a == 3:
                return a+1
            elif a == 2 or a == 4:
                return a

def main_menu(screen):
    one_time = 0
    a = 1
    while True:
        a = 1
        DISPLAYSURF.fill(green)
        pygame.draw.rect(DISPLAYSURF,red,(750,800,200,100))
        fontObj = pygame.font.Font('freesansbold.ttf', 24)
        textSurfaceObj = fontObj.render('Start 1p', True, win1, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (850, 850)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(DISPLAYSURF,red,(750,600,200,100))
        fontObj = pygame.font.Font('freesansbold.ttf', 24)
        textSurfaceObj = fontObj.render('Start 4p', True, win1, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (850, 650)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(DISPLAYSURF,red,(550,400,200,100))
        fontObj = pygame.font.Font('freesansbold.ttf', 24)
        textSurfaceObj = fontObj.render('Start 2p_team', True, win1, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (650, 450)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(DISPLAYSURF,red,(950,400,200,100))
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        fontObj = pygame.font.Font('freesansbold.ttf', 24)
        textSurfaceObj = fontObj.render('Start 2p_rival', True, win1, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1050, 450)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(DISPLAYSURF,red,(750,200,200,100))
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        fontObj = pygame.font.Font('freesansbold.ttf', 24)
        textSurfaceObj = fontObj.render('Start 3p', True, win1, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (850, 250)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        fontObj = pygame.font.Font('freesansbold.ttf', 64)
        textSurfaceObj = fontObj.render('Card Game', True, win1, green)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (850, 50)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        pygame.display.set_caption('Card Game')
        for event in pygame.event.get():
            just = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and one_time == 0:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > 750 and mouse[0] < 950 and mouse[1] > 600 and mouse[1] < 700:
                    DISPLAYSURF.fill(green)
                    while True:
                        a = game_4p(DISPLAYSURF,a,0)
                        if a == 0:
                            break
                    one_time = 0
                if mouse[0] > 750 and mouse[0] < 950 and mouse[1] > 200 and mouse[1] < 300:
                    DISPLAYSURF.fill(green)
                    while True:
                        a = game_3p(DISPLAYSURF,a,0)
                        if a == 0:
                            break
                    one_time = 0
                if mouse[0] > 550 and mouse[0] < 750 and mouse[1] > 400 and mouse[1] < 500:
                    DISPLAYSURF.fill(green)
                    while True:
                        a = game_2p_team(DISPLAYSURF,a,0)
                        if a == 0:
                            break
                    one_time = 0
                if mouse[0] > 950 and mouse[0] < 1150 and mouse[1] > 400 and mouse[1] < 500:
                    DISPLAYSURF.fill(green)
                    while True:
                        a = game_2p_rival(DISPLAYSURF,a,0)
                        if a == 0:
                            break
                    one_time = 0
                if mouse[0] > 750 and mouse[0] < 950 and mouse[1] > 800 and mouse[1] < 900:
                    DISPLAYSURF.fill(green)
                    while True:
                        a = game_1p(DISPLAYSURF,a,0)
                        if a == 0:
                            break
                    one_time = 0
            pygame.display.update()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1600,1000))
green = (0,0,0)
win1 = (255,255,255)
win2 = (0,0,255)
red = (255,0,0)
a = 1
main_menu(DISPLAYSURF)
pygame.display.update()
