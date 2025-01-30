import pygame
from Player import *

pygame.init()

win_size = 500
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("ToNk")


pixel_size = 20

run = True
game_speed = 150

background = pygame.image.load("images/screen.png")
tank = pygame.image.load("images/tank_b.png")
tank1 = Player(60, 60, tank, "tile_b")
tank2 = Player(200, 200, tank, "tile_b", pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_e)

def draw_window():

    win.blit(background, (0,0))
    tank1.draw(win)
    tank2.draw(win)
    pygame.display.update()


    # Main Loop

while run:
    pygame.time.delay(game_speed)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] :
            run = False


        # Movement
    tank1.handle_input(keys)
    tank2.handle_input(keys)

    tank1. update_movement()
    tank2. update_movement()

    
    draw_window()



pygame.quit()