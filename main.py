import pygame
from Player import *
from collider_manager import *

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
tanks = [tank1, tank2]
objects_collision = CollisionManager(tanks) 

def draw_window():

    win.blit(background, (0,0))

    for tank in tanks:
        tank.draw(win)

    objects_collision.Tank_Got_Hit()
    pygame.display.update()


    # Main Loop

while run:
    pygame.time.delay(game_speed)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] :
            run = False

    for tank in tanks:
        if tank.health == 0 :
            tank.__del__()
            tanks.pop(tanks.index(tank))

        # Movement
    for tank in tanks:
        tank.handle_input(keys)

    objects_collision = CollisionManager(tanks)

    for tank in tanks:
        if not objects_collision.is_collided():
            tank. update_movement()


    draw_window()



pygame.quit()