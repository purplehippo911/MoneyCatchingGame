import pygame


coin_1_x = 0
coin_1_y = 2

coin_2_x = 0
coin_2_y = 2

# vanlig funksjon
myFunction()


# metode
coin.draw()

# object
coin1 = Coin(100, 500, )
coin2 = Coin(200, 400)
coin1.x

coin1.x

coin2.x = True

coin3.x = False

class Coin(object):
    # image
    coin_char = pygame.image.load('./src/assets/sprites/gdm-coin/Coin.gif')

    def __init__(self, width, height, window_width, window_height, vel, coin_char = coin_char):
        self.x = window_width / 2
        self.y = window_height
        self.width = width
        self.height = height
        self.vel = vel
        self.hitbox = (self.x + 5, self.y + 11, self.width, self.height)


    def draw(self, win, window_height):
        # display coin to the screen
        win.blit(self.coin_char, (self.x, self.y))

        # hitbox
        self.hitbox = (self.x + 5, self.y + 11, self.width, self.height)

        # make coin descend automatically
        original_y = window_height / 2 - window_height
    
        self.y += self.vel
        if self.y + self.height >= window_height:
            self.y = original_y
