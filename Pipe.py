import pygame
pygame.init()

PIPE_IMAGE = pygame.image.load("tube.png")

class Pipe(pygame.sprite.Sprite):

    def __init__(self, flipped, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = PIPE_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (1920 / 2, 1080 / 2)
        self.rect.x = 2100
        self.rect.y = y
        self.image.set_colorkey((0,0,0))
        self.flipped = flipped
        if flipped:
            self.image = pygame.transform.flip(self.image, False, True)

    def update(self):
        self.rect.x -= 20
        if self.rect.x <= -500:
            self.kill()