import pygame
import time
from src.sprites.player import Player
from src.sprites.coin import Coin
pygame.init()

# attributes
pygame.display.set_caption("Money Catch")

# window
window_height = 1500
window_width = 1500
win = pygame.display.set_mode((window_width,window_height))

# images
window_bg = pygame.image.load('./src/assets/img/game.png')
main_char_big = pygame.image.load('./src/assets/sprites/safe_box/pngs/safes/safe_short_green_open.png')
coin_char = pygame.image.load('./src/assets/sprites/gdm-coin/Coin.gif')

# Set the size for the image
char_width = main_char_big.get_rect().width
char_height = main_char_big.get_rect().height

# Scale the image to the needed size
main_char = pygame.transform.scale(main_char_big, (char_width/10, char_height/10))

## clock - time frame
clock = pygame.time.Clock()

## redraw window function
def redrawGameWindow():
    win.blit(window_bg, (0, 0))
    win.blit(main_char, (player.x, player.y))
    win.blit(coin_char, (coin.x, coin.y))
    win.blit(coin_char, (coin2.x, coin2.y))
    win.blit(coin_char, (coin3.x, coin3.y))
    win.blit(coin_char, (coin4.x, coin4.y))
    pygame.display.flip()


    pygame.display.update() 


# main game loop
player = Player(40, 60, window_width, window_height)
coin = Coin(40, 60, window_width + 500, window_height, 8)
coin2 = Coin(40, 60, window_width - 200, window_height + 50, 7)
coin3 = Coin(40, 60, window_width - 1000, window_height + 120, 6)
coin4 = Coin(40, 60, window_width + 1000, window_height + 150, 5)
run = True

while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key movements
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel

    elif keys[pygame.K_RIGHT] and player.x < window_width - player.vel - player.width:
        player.x += player.vel
    
    # coin drop 1
    original_y = window_height / 2 - window_height
    
    coin.y += coin.vel
    if coin.y + coin.height >= window_height:
        coin.y = original_y
        #run = False

    # coin drop 2
    coin2.y += coin2.vel
    if coin2.y + coin2.height >= window_height:
        coin2.y = original_y
        #run = False

    # coin drop 3
    coin3.y += coin3.vel
    if coin3.y + coin3.height >= window_height:
        coin3.y = original_y
   
    # coin drop 4
    coin4.y += coin4.vel
    if coin4.y + coin4.height >= window_height:
        coin4.y = original_y

    redrawGameWindow()

pygame.quit()