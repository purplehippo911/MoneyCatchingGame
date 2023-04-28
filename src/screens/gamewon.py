import pygame

def draw_game_won(win, window_width, window_height):
    window_bg = pygame.image.load("src/assets/img/cyberpunk-street.png")
    
    pygame.mixer.music.load('jazz.wav')
    pygame.mixer.music.play(-1)
    
    win.blit(window_bg, (0, 0))
    win.fill((0, 0, 0))
    
    # fixing text and font
    font = pygame.font.SysFont('comicsans', 40)
    title = font.render('Congratulations, you won!', True, (255, 255, 255))
    info = font.render('You got 10 000 dollars, enough to start a business!', True, (255, 255, 255))
    restart_button = font.render('Press R to try again.', True, (255, 255, 255))
    quit_button = font.render('Press Q to try quit.', True, (255, 255, 255))

    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(info, (window_width/2 - info.get_width()/2, window_height/2 + info.get_height()/2))
    win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_width/2 + restart_button.get_height()/2))
    win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_width/2 + quit_button.get_height()*2))
