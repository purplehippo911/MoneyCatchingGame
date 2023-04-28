import pygame, random

class Bomb(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    def __init__(self, window_width):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(self.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = 0

    def update(self, score, window_height):
        self.rect.y += 5
        if self.rect.y > window_height:
            self.kill()
            score -= 1
