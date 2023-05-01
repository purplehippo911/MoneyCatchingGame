import pygame        

# character
class Player(object):
    main_char_big = pygame.image.load('./src/assets/sprites/safe_box/pngs/safes/safe_short_green_open.png')

    # Set the size for the image
    char_width = main_char_big.get_rect().width
    char_height = main_char_big.get_rect().height

    # Scale the image to the needed size
    main_char = pygame.transform.scale(main_char_big, (char_width/10, char_height/10))

    def __init__(self, width, height, window_width, window_height):
        self.width = width
        self.height = height
        self.vel = 10
        self.x = window_width / 2 - width * 3
        self.y = window_height / 2 + height * 3 - self.vel * 3
        self.hitbox = (self.x + 11, self.y + 11, self.width, self.height)

    def draw(self, win):
        # add character to screen
        win.blit(self.main_char, (self.x, self.y))
        
        # hitbox
        self.hitbox = (self.x + 11, self.y + 11, self.width, self.height)

    def hit(self):  # This will display when the enemy is hit
        print('hit')