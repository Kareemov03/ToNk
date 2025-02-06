import pygame

class CollisionManager():
    def __init__(self, tanks):

        self.tanks = tanks

            # Bullet Width & Height
        self.bullet_dimentions = 20
            # Player Width & Height
        self.Player_dimentions = 60

        self.bullet_index = 0

    def __Bullet_Hit(self, bulletsA, tankB):
         
         for bullet in bulletsA:
              if bullet.y in range(tankB.y, tankB.y + self.Player_dimentions):
                if bullet.x in range(tankB.x, tankB.x + self.Player_dimentions):
                    self.bullet_index = bulletsA.index(bullet)
                    return True


    def Tank_Got_Hit(self):

        for i in range(len(self.tanks)):
            for j in range(len(self.tanks)):
                    if i != j:
                        if self.__Bullet_Hit(self.tanks[i].bullets, self.tanks[j]):
                             self.tanks[j].Bullet_recive_damage(True)
                             self.tanks[i].Tank_give_damage(True, self.bullet_index)
    
    def is_collided(self):

        for i in range(len(self.tanks)):
            for j in range(len(self.tanks)):
                if i != j:
                    if  (self.tanks[i].next_move_xmin < self.tanks[j].next_move_xmax
                          and self.tanks[i].next_move_xmax > self.tanks[j].next_move_xmin 
                          and self.tanks[i].next_move_ymin < self.tanks[j].next_move_ymax
                            and self.tanks[i].next_move_ymax > self.tanks[j].next_move_ymin):
                            return True
                    else : return False
                

                