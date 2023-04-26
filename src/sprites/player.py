import pygame        

# character
class Player(object):
    def __init__(self, width, height, window_width, window_height, ):
        self.width = width
        self.height = height
        self.vel = 6
        self.x = window_width / 2 - width * 3
        self.y = window_height / 2 + height * 3 - self.vel * 3
