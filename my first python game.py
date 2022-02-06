# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,500))

pygame.display.set_caption("Space Invaders by Godspower")

background = pygame.image.load('static/Space Wallpaper Background.jpg ')

mixer.music.load("static/alexander-nakarada-chase.mp3")
mixer.music.play(-1)

#score font size
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)
textX =10
textY = 10

#gameover font
over_font = pygame.font.Font('freesansbold.ttf', 90)


#player config
playerImg = pygame.image.load('static/ufo.png')
playerX = 390
playerY = 400
steps = 0

#enemy list
enemyImg = []
enemyX = []
enemyY = []
enemy_steps = []
enemy_y_steps = []
num_enemies = 10
explosion_sound = mixer.Sound("static/Explosion+1 (mp3cut.net).mp3")
bullet_sound = mixer.Sound("static/heat-vision-1 (mp3cut.net) (2).mp3")
#creating n numbers of enemies and populating each list

for i in range(num_enemies): 

    enemyImg.append(pygame.image.load('static/foot-clan.png'))
    enemyX.append(random.randint(0,766))
    enemyY.append(random.randint(40,120))
    enemy_steps.append(0.3)
    enemy_y_steps.append(5)

#loading bullet images
    
bullet = pygame.image.load('static/bullet (3).png')
bulletX = 0
bulletY = 368
bullet_y_change = 2
bullet_state = "ready"

def show_score(x,y):
    score = font.render('score:'+str(score_value), True, (199,199,199))
    screen.blit(score, (x,y))
    
def game_over_text():
    over_text = over_font.render('GAME OVER!', True, (199,199,199))
    screen.blit(over_text, (100,200)) 
    
def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+2,y+10))
    
def iscollision(enemyX,bulletX,enemyY,bulletY):
    dist = math.sqrt(math.pow( enemyX-bulletX  ,2) + math.pow( enemyY-bulletY , 2))
    if dist < 27:
        return True
    
    
main = True

while main:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main=False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                steps += 0.4
            if event.key == pygame.K_LEFT:
                steps -= 0.4
            if event.key == pygame.K_q:
                main = False
                break
            if event.key == pygame.K_SPACE:
                if bullet_state =="ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key ==\
            pygame.K_LEFT:
                steps = 0
                
    playerX += steps
    
    
  
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 766:
        playerX = 766 
        
    
    for i in range(num_enemies):
        if enemyY[i] >=350:
            for m in range(num_enemies):
                enemyY[m] = 2000
            game_over_text()
            break
    
        
    for i in range(num_enemies):    
        enemyX[i] += enemy_steps[i]
        if enemyX[i] <= 0:
            enemy_steps[i] = 1
            enemyY[i] += enemy_y_steps[i]
        elif enemyX[i] >= 766:
            enemy_steps[i] = -1
            enemyY[i] += enemy_y_steps[i]

        collision = iscollision(enemyX[i],bulletX,enemyY[i],bulletY) 
        
        if collision:
            explosion_sound.play()
            bulletY = 368
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,766)
            enemyY[i] = random.randint(40,120)
        enemy(enemyX[i],enemyY[i])
    
    if bulletY <=0:
        bulletY= 368
        bullet_state = "ready"
        
    if bullet_state == "fire":
        bullet_sound.play()
        fire_bullet(bulletX,bulletY)
        bulletY -= bullet_y_change
        
    show_score(textX,textY)
           
    player(playerX,playerY)
  
    pygame.display.update()