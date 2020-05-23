import pygame as pg
import math
import random

pg.init()
width, height= 640, 480
screen=pg.display.set_mode((width,height))

acc=[0,0]
arrows=[]

badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

keys=[False,False,False,False]
playerpos=[100,100]
spd=5

player=pg.image.load("resources/images/dude.png")
grass=pg.image.load("resources/images/grass.png")
castle=pg.image.load("resources/images/castle.png")
arrow=pg.image.load("resources/images/bullet.png")
badguyimg1 = pg.image.load("resources/images/badguy.png")
badguyimg=badguyimg1

while 1:
    screen.fill(0)
    for x in range((int)(width/grass.get_width()+1)):
        for y in range((int)(height/grass.get_height()+1)):
            screen.blit(grass,(x*grass.get_width(),y*grass.get_height()))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    position = pg.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pg.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pg.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    if badtimer==0:
        badguys.append([640,random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer+=5
    idx=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(idx)    
        badguy[0]-=7
        badrect=pg.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue-=random.randint(5,20)
            badguys.pop(idx)
        index1=0
        for bullet in arrows:
            bullrect=pg.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                acc[0]+=1
                badguys.pop(idx)
                arrows.pop(index1)
        idx+=1
    for badguy in badguys:
        screen.blit(badguyimg,badguy)
    pg.display.flip()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit(0)
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_w:
                keys[0]=True
            elif event.key==pg.K_a:
                keys[1]=True
            elif event.key==pg.K_s:
                keys[2]=True
            elif event.key==pg.K_d:
                keys[3]=True
        if event.type==pg.KEYUP:
            if event.key==pg.K_w:
                keys[0]=False
            elif event.key==pg.K_a:
                keys[1]=False
            elif event.key==pg.K_s:
                keys[2]=False
            elif event.key==pg.K_d:
                keys[3]=False
        if event.type==pg.MOUSEBUTTONDOWN:
            position=pg.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
    if keys[0]:
        playerpos[1]-=spd
    elif keys[2]:
        playerpos[1]+=spd
    if keys[1]:
        playerpos[0]-=spd
    elif keys[3]:
        playerpos[0]+=spd
    
    badtimer-=1
