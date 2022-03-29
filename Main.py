from tkinter import CENTER
import pygame
from pygame.locals import *
import sys, random
import Pipe
import Bird

pygame.init()
win = pygame.display.set_mode((1920,1080))
bg_img = pygame.image.load("space_BG.png")
bg = pygame.transform.scale(bg_img,(1920, 1080))
width = 1920
i = 0
x = 300
y= 540
radius = 15
vel_x = 10
vel_y = 10
jump = False

pipe_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player = Bird.bird()
player_group.add(player)




def spawnPipe():
    y = random.randint(-200, 400)
    tPipe = Pipe.Pipe(False, y)

    y = random.randint(600, 1080)
    bPipe = Pipe.Pipe(True, y)

    pipe_group.add(tPipe)
    pipe_group.add(bPipe)

spawnPipe()

while True:
    for event in pygame.event.get():...


############### BackGround ###################
    win.fill((0,0,0))
    win.blit(bg, (i ,0))
    win.blit(bg, (width+i, 0))

    if i == -width:
        win.blit(bg, (width+i, 0))
        i = 0
    i -= 1

#############################################

    player_group.update()
    player_group.draw(win)

    pipe_group.update()
    pipe_group.draw(win)    

    for pipe in pipe_group:
        if pipe.rect.x == x:
            spawnPipe()
            break

    if pygame.sprite.groupcollide(player_group, pipe_group, False, False):
        print("Player hit a pipe!")
    
    pygame.time.delay(30) #Game speed lower to increase, increas to slow
    pygame.display.update()

    if event.type == QUIT:
        pygame.quit
        sys.exit()

