import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))

BIRD_IMAGE = pygame.image.load("bird.png")

class bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = BIRD_IMAGE
        self.image = pygame.transform.scale(BIRD_IMAGE, (200,200))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (1920 / 2, 1080 / 2)
        self.rect.x = 300
        self.rect.y = 540
        self.jump = False
        self.vel_y = 10
        self.vel_x = 10

    def update(self):
        userInput = pygame.key.get_pressed() # Init Keypress


        self.rect.y += self.vel_y * 1.5

        if self.jump is False and userInput[pygame.K_SPACE]: #Jump key
            self.jump = True

        if self.jump is True:
            self.rect.y -= self.vel_y * 4  # Jump height
            self.vel_y -= 1   
            if self.vel_y < -10: 
                self.vel_y = 10 + 3
                self.jump = False

    