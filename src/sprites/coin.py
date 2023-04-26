import pygame

class Coin(object):
    def __init__(self, width, height, window_width, window_height, vel):
        self.x = window_width / 2
        self.y = window_height / 2 - 100 * 2
        self.width = width
        self.height = height
        self.vel = vel

