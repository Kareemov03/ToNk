import pygame

class CollisionManager():
    def __init__(self, A_position_x, A_position_y, B_position_x, B_position_y):

        self.A_positionx = A_position_x
        self.A_positiony = A_position_y

        self.B_positionx = B_position_x
        self.B_positiony = B_position_y
        