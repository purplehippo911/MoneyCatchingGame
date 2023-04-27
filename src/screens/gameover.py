import pygame

def draw_game_over(win, window_width, window_height):
    window_bg = pygame.image.load("src/assets/img/cyberpunk-street.png")
    
    win.blit(window_bg, (0, 0))
    win.fill((0, 0, 0))
    
    # fixing text and font
    font = pygame.font.SysFont('comicsans', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('Press R to try again.', True, (255, 255, 255))
    quit_button = font.render('Press Q to try quit.', True, (255, 255, 255))

    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_width/2 + restart_button.get_height()/2))
    win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_width/2 + quit_button.get_height()*2))
