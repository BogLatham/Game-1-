import pygame
from pygame.locals import *
import sys

pygame.init()
window = pygame.display.set_mode((1920,1080))
bg_img = pygame.image.load("space_BG.png")
bg = pygame.transform.scale(bg_img,(1920, 1080))
width = 1920
i = 0



while True:
    for event in pygame.event.get():...

    window.fill((0,0,0))
    window.blit(bg, (i ,0))
    window.blit(bg, (width+i, 0))

    if i == -width:#
        window.blit(bg, (width+i, 0))
        i = 0
    i -= 0.2


    pygame.display.update()

    if event.type == QUIT:
        pygame.quit
        sys.exit()

