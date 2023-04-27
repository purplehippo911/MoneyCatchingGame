import pygame

def draw_start_menu(win, window_width, window_height):
    win.fill((255, 255, 255))
    
    # fixing text and font
    font = pygame.font.SysFont('comicsans', 40)
    title = font.render('Money Rain', True, (0, 0, 0))
    start_button = font.render('Start', True, (0, 0, 0))

    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(start_button, (window_width/2 - start_button.get_width()/2, window_width/2 + start_button.get_height()/2))
