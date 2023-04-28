import pygame
from pygame import mixer
pygame.init()
from src.sprites.button import Button

# setting up audio
mixer.music.set_volume(0.5)
pygame.mixer.music.load('src/assets/audio/Gregor Quendel - Cinematic Trailer Music/Gregor Quendel - Cinematic Trailer Music/Gregor Quendel - Cinematic Trailer Music - 01 - Cinematic Piano Trailer.wav')

def draw_start_menu(win, window_width, window_height):
    win.fill((0, 100, 100))
    mixer.music.stop()
    mixer.music.play(1)
    # fixing text and font
    title_font = pygame.font.SysFont('comicsans', 50)
    text_font = pygame.font.SysFont('comicsans', 30)
    title = title_font.render('Money Rain', True, (255, 255, 255))
    start_button = text_font.render('Press "Spacebar" to start', True, (0, 0, 0))

    # making button object
    """
    game_state = "start_game"
    def buttonPressed():
        game_state = "game"
    Button(30, 30, 400, 100, 'Button One (onePress)', buttonPressed())
    """
    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(start_button, (window_width/2 - start_button.get_width()/2, window_width/2 + start_button.get_height()/2))
