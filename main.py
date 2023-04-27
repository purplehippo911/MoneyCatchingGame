import pygame
# importing audio module
from pygame import mixer

# importing sprites
from src.sprites.player import Player
from src.sprites.coin import Coin

# importing screens, both start and end screen
from src.screens.start import draw_start_menu
from src.screens.gameover import draw_game_over

pygame.init()

# attributes
pygame.display.set_caption("Money Catch")
logo = pygame.image.load("src/assets/sprites/Coins/Coin Purses Sampler/Original Diminsions/Pattern Blue/Open.png")
pygame.display.set_icon(logo)

# window and background image
window_height = 1500
window_width = 1500
win = pygame.display.set_mode((window_width,window_height))
window_bg = pygame.image.load('./src/assets/img/game.png')

# clock - time frame
clock = pygame.time.Clock()

# sum
score = 20

# text for sum
font = pygame.font.SysFont("comicsans", 30, True)

# setting up audio
mixer.init()
mixer.music.load("src/assets/audio/coin_money_2.wav")
mixer.music.set_volume(0.9)

game_state = "start_menu"

## redraw window function
def redrawGameWindow():
    # game state
    if game_state == "start_menu":
        draw_start_menu(win, window_width, window_height)
    elif game_state == "game":
        win.blit(window_bg, (0, 0))
        # draw character sprite to the screen
        player.draw(win)
        # drawing coins to the screen
        for coin in coins:
            coin.draw(win, window_height)

        pygame.display.flip()

        # Create a text surface with the font object
        text = font.render(f"Score: {str(round(score))}", 1, (255, 255, 255))

        # Blit the text surface onto the screen surface
        win.blit(text, (player.x, player.y))
    elif game_state == "game_over":
        draw_game_over(win, window_width, window_height)
    pygame.display.update() 

# objects for coins and player
player = Player(120, 80, window_width, window_height)
coin = Coin(20, 20, window_width + 500, window_height, 8)
coin2 = Coin(20, 20, window_width - 200, window_height + 50, 7)
coin3 = Coin(20, 20, window_width - 1000, window_height + 120, 6)
coin4 = Coin(20, 20, window_width + 1000, window_height + 150, 5)

# list cointaining all coins, so that I can iterate over items
coins = [coin, coin2, coin3, coin4]

# main game loop
run = True
while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # key movements
    keys = pygame.key.get_pressed()

    if game_state == "start_menu":
        if keys[pygame.K_SPACE]:
            game_state = "game"
    elif game_state == "game":
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel

        elif keys[pygame.K_RIGHT] and player.x < window_width - player.vel - player.width:
            player.x += player.vel
        elif keys[pygame.K_q]:
            pygame.quit()
    else:
        if keys[pygame.K_q]:
            pygame.quit()
        elif keys[pygame.K_r]:
            game_state = "game"
            score = 0
            for coin in coins:
                coin.y = 0
            redrawGameWindow()
   

    # checking for collision between character and coin
    for coin in coins:
        if coin.y - coin.width < player.hitbox[1] + player.hitbox[3] and coin.y + coin.width > player.hitbox[1]: # checks x coords
            if coin.x + coin.width > player.hitbox[0] and coin.x - coin.width < player.hitbox[0] + player.hitbox[2]: # Checks y coords
                coin.draw(win, window_height)
                # playing the coin audio
                score += 5
                mixer.music.play()
            else:
                if score > 0:
                    score -= 1
                elif score == 0:
                    game_state = "game_over"

    redrawGameWindow()

pygame.quit()