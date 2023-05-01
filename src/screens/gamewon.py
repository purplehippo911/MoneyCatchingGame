import pygame

def draw_game_won(win, window_width, window_height):
    
    # fixing text and font
    font = pygame.font.SysFont('comicsans', 40)

    title = font.render('Congratulations, you won!', True, (255, 255, 255))
    info = font.render('You got 10 000 dollars, enough to start a business!', True, (255, 255, 255))
    advice = font.render('Now, go out and touch some grass', True, (50, 255, 20))
    author = font.render('Made my Purplehippo911', True, (0, 255, 120))
    restart = font.render('Press R to try again.', True, (255, 255, 255))
    quit = font.render('Press Q to try quit.', True, (255, 255, 255))

    # displaying to screen
    win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/2))
    win.blit(info, (window_width/2 - info.get_width()/2, window_width/2 - info.get_height()/2 + 60))
    win.blit(advice, (window_width/2 - advice.get_width()/2, window_height/2 - advice.get_height()/2 + 120))
    win.blit(author, (window_width/2 - author.get_width()/2, window_width/2 - author.get_height()/2 + 180))
    win.blit(restart, (window_width/2 - restart.get_width()/2, window_height/2 - restart.get_height()/2 + 240))
    win.blit(quit, (window_width/2 - quit.get_width()/2, window_width/2 - quit.get_height() + 320))
