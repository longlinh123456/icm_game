import pygame, sys

pygame.init
win_size = height, width = 500, 500
background = [0,0,0]
running = True
window = pygame.display.set_mode(win_size)
while running == True:
    window.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.flip()
