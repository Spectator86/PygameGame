from entity import Entity
import pygame as pg

class Player(Entity):
    def __init__(self, speed, x, y, scale_x, scale_y, file, angle=0):
        self.speed = speed
        super().__init__(x, y, scale_x, scale_y, file, angle=0)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.rect.y += self.speed
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.rect.x += self.speed