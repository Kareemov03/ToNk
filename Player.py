import pygame

pixel_size = 20

class Player(object):
    def __init__(self, x, y, tank, tile_name, K_up= pygame.K_UP, K_down= pygame.K_DOWN, K_left= pygame.K_LEFT, K_right= pygame.K_RIGHT, K_shoot= pygame.K_SPACE):
            # Position
        self.x = x
        self.y = y
            # Image
        self.tank = tank
            # Tank Name
        self.tile_name = tile_name
        self.tile = pygame.image.load(f"images/{tile_name}.png")

            # Rotation
         # -1 == left || 1 == right
         # -1 == down || 1 == up
        self.direction = [1,0]
        self.look_direction = [1,0]

        self.K_up = K_up
        self.K_down = K_down
        self.K_left = K_left
        self.K_right = K_right
        self.K_shoot = K_shoot


        global pixel_size
        self.win_size = 500
        
        self.bullets = []
        self.bullet_speed = 3

        self.health = 3
        self.heart = pygame.image.load("images/heart.png")
        self.alpha = 255
        self.fade = True

    def __del__(self):
        pass

        
    @property
    def next_move_xmax(self):
        return self.x + (pixel_size * self.direction[0]) + self.tank.get_width()
    @property
    def next_move_xmin(self):
        return self.x + (pixel_size * self.direction[0])
    @property
    def next_move_ymax(self):
        return self.y + (pixel_size * self.direction[1]) + self.tank.get_height()
    @property
    def next_move_ymin(self):
        return self.y + (pixel_size * self.direction[1])

    def draw(self, win):

        if self.look_direction == [-1, 0] :
            win.blit(self.tank, (self.x,self.y))
        elif self.look_direction == [1, 0]:
            win.blit(pygame.transform.rotate(self.tank, 180), (self.x, self.y))
        elif self.look_direction == [0, -1]:
            win.blit(pygame.transform.rotate(self.tank, -90), (self.x, self.y))
        elif self.look_direction== [0, 1]:
            win.blit(pygame.transform.rotate(self.tank, 90), (self.x, self.y))

        for bullet in self.bullets:
            bullet.draw(win)
            if bullet.projectile_travel_distance <= 0:
                self.bullets.pop(self.bullets.index(bullet))

        for i in range(self.health):
            win.blit(self.heart, (self.x + (pixel_size * i), self.y + 60))

        if self.fade:
            self.alpha -= 20
            self.heart.set_alpha(max(0,self.alpha))


    def handle_input(self, key):

        if key[self.K_left]:

            self.direction = self.look_direction = [-1, 0]

        elif key[self.K_right]:

            self.direction = self.look_direction = [1, 0]

        elif key[self.K_up]:

            self.direction = self.look_direction = [0, -1]

        elif key[self.K_down]:

            self.direction = self.look_direction = [0, 1]

        else: 
            self.direction = [0,0]
        
        if key[self.K_shoot]:

            self.launch_projectile()


    def update_movement(self):

            self.x += self.direction[0] * pixel_size
            self.x %= self.win_size - self.tank.get_width() + pixel_size

            self.y += self.direction[1] * pixel_size
            self.y %= self.win_size - self.tank.get_height() + pixel_size

    def launch_projectile(self):

        xy = self.get_bullet_spawn_point()
        if len(self.bullets) <= 3 :
            self.bullets.append(Projectiles(xy[0], xy[1], self.tile, self.look_direction, self.bullet_speed))

    def get_bullet_spawn_point(self):

        return (self.x + (self.tank.get_width() * 1/3), self.y + (self.tank.get_height() * 1/3))

    def Bullet_recive_damage(self, hit):
            # "if this tank got hit by a bullet"
       if hit:
              self.health -= 1
              self.alpha = 255

    def Tank_give_damage(self, hit, bullet_index):
            # "if this tank hit another tank with a bullet"
        if hit:
            self.bullets.pop(bullet_index)




class Projectiles(object):
    def __init__(self, x, y, tile, look_direction, velocity): 
            # Position
        self.x = x
        self.y = y
            # Image
        self.tile = tile
        self.velocity = velocity
        self.look_direction = look_direction

        global pixel_size
        self.projectile_travel_distance = 15 # in pixel

    def update_movement(self):

        self.x += self.look_direction[0] * self.velocity * pixel_size

        self.y += self.look_direction[1] * self.velocity * pixel_size

        self.projectile_travel_distance -= self.velocity        

    def draw(self, win):

        self.update_movement()
        win.blit(self.tile, (self.x,self.y))