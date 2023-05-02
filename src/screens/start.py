import pygame
from pygame import mixer
pygame.init()
from src.sprites.button import Button

# setting up audio
mixer.music.set_volume(0.7)

def draw_start_menu(win, window_width, window_height):
    win.fill((0, 100, 100))

    # fixing font
    title_font = pygame.font.SysFont('comicsans', 50)
    text_font = pygame.font.SysFont('comicsans', 30)

    description_font = pygame.font.SysFont('comicsans', 30)
    
    # rendering text
    title = title_font.render('Catching Money', True, (255, 255, 255))
    start_text = text_font.render('Press "Spacebar" to start', True, (255, 255, 255))
    
    description_1 = "Catch coins falling from the sky. Use 'left' and 'right' arrows to move."
    description_text_1 = description_font.render(description_1, True, (0, 0, 0))

    description_2 = "Avoid the red bombs, that comes later on. Get score to 1000 to win."
    description_text_2 = description_font.render(description_2, True, (0, 0, 0))

    # making button object
    """
    game_state = "start_game"
    def buttonPressed():
        game_state = "game"
    Button(30, 30, 400, 100, 'Button One (onePress)', buttonPressed())
    """
    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(description_text_1, (window_width/2 - description_text_1.get_width()/2, window_width/2 + description_text_1.get_height()/2))
    win.blit(description_text_2, (window_width/2 - description_text_2.get_width()/2, window_width/2 + description_text_2.get_height()/2 + 50))
    win.blit(start_text, (window_width/2 - start_text.get_width()/2, window_width/2 + start_text.get_height()/2 + 80))
