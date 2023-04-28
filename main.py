import pygame
# importing audio module
from pygame import mixer

# importing sprites
from src.sprites.player import Player
from src.sprites.coin import Coin
from src.sprites.bomb import Bomb

# importing screens, both start and end screen
from src.screens.start import draw_start_menu
from src.screens.gameover import draw_game_over
from src.screens.gamewon import draw_game_won

pygame.init()

# attributes
pygame.display.set_caption("Money Catch")
logo = pygame.image.load("src/assets/sprites/Coins/Coin Purses Sampler/Original Diminsions/Pattern Blue/Open.png")
pygame.display.set_icon(logo)

# window and background image
window_height = 1500
window_width = 1500
win = pygame.display.set_mode((window_width,window_height), pygame.RESIZABLE)
window_bg = pygame.image.load('./src/assets/img/game.png')

# clock - time frame
clock = pygame.time.Clock()

# sum
score = 20
max_score = 10000

# text for sum
font = pygame.font.SysFont("comicsans", 35, True)

# setting up audio
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

        # Spawn a new bomb every 50 frames
        if score < max_score / 20 and pygame.time.get_ticks() % 50 == 0:
            new_bomb = Bomb(window_width)
            bomb_group.add(new_bomb)
        
        # Update the bombs
        bomb_group.update(score, window_height)

        bomb_group.draw(win)

        pygame.display.flip()

        # Create a text surface with the font object
        text = font.render(f"Score: {str(round(score))}", 1, (255, 255, 255))

        # Blit the text surface onto the screen surface
        win.blit(text, (window_width / 2 + 390, window_height/2 - 300))
    elif game_state == "game_over":
        draw_game_over(win, window_width, window_height)
    else:
        draw_game_won(win, window_width, window_height)
    pygame.display.update() 

# objects for coins and player
player = Player(120, 80, window_width, window_height)
coin = Coin(20, 20, window_width + 500, window_height, 8)
coin2 = Coin(20, 20, window_width - 200, window_height + 50, 7)
coin3 = Coin(20, 20, window_width - 1000, window_height + 120, 6)
coin4 = Coin(20, 20, window_width + 1000, window_height + 150, 5)
# list cointaining all coins, so that I can iterate over items
coins = [coin, coin2, coin3, coin4]

# Create the sprite group for the bombs
bomb_group = pygame.sprite.Group()
isBombsVisible = False

# main game loop
run = True
while run:
    clock.tick(40)

    ## events and button events
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
            score = 20
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
                mixer.Channel(0).play(mixer.Sound('src/assets/audio/coin_sound/coin_money_2.wav'))
            else:
                mixer.Channel(1).play(mixer.Sound('src/assets/audio/8-bit sounds/8bit-damage22.wav'))
                if score > 0 and score <= max_score:
                    score -= 1
                elif score <= 0:
                    game_state = "game_over"
                    mixer.music.stop()
                    mixer.Channel(0).stop()
                    mixer.Channel(1).stop()
                    for coin in coins:
                        coin.y = 0
                    redrawGameWindow()
                    mixer.music.load('src/assets/audio/sci-fi sounds/Rover_Fail_Stereo_01.wav')
                    mixer.music.play(-1)


                elif score == max_score:
                    game_state = "game_won"
                    mixer.music.stop()
                    mixer.Channel(0).stop()
                    mixer.Channel(1).stop()
                    for coin in coins:
                        coin.y = 0
                    redrawGameWindow()
   
        # checking for collision between bomb and player
        for bomb in bomb_group:
            if bomb.rect.y < player.hitbox[1] + player.hitbox[3] and bomb.rect.y > player.hitbox[1]: # checks x coords
                    if bomb.rect.x > player.hitbox[0] and bomb.rect.x < player.hitbox[0] + player.hitbox[2]: # Checks y coords
                        bomb.update(score, window_height)
                        score-=10
                        # playing the coin audio
                        mixer.Channel(1).play(mixer.Sound('src/assets/audio/8-bit sounds/8bit-damage22.wav'))

    ## harder modes
    runOnce = True
    for coin in coins:
        if score >= round(max_score / 20):
            coin.vel+=2
            player.vel+=3
            isBombsVisible = True
            redrawGameWindow()
        elif score >= round(max_score / 10):
            coin.vel += 5
            player.vel += 5
            

    redrawGameWindow()

pygame.quit()