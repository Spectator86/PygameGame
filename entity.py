import pygame as pg
from settings import *


class Entity:
    def __init__(self, x, y, scale_x, scale_y, file, angle=0):
        # Variables
        self.scale_x = scale_x
        self.scale_y = scale_y

        self.angle = angle

        # Load and transform image
        self.image = pg.image.load(file).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.scale_x, self.scale_y))
        self.image = pg.transform.rotate(self.image, self.angle)

        # Creating RECT
        self.rect = self.image.get_rect(topleft=(x, y))

    # Draw on display
    def draw(self, sc):
        sc.blit(self.image, (self.rect.x + SCROLL_X, self.rect.y + SCROLL_Y))

    # Transform function
    def transform_scale(self, scale_x, scale_y):
        # Scaling
        self.image = pg.transform.scale(self.image, (scale_x, scale_y))

        # Update RECT
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    def rotate_transform(self, angle):
        # Rotating
        self.image = pg.transform.rotate(self.image, self.angle)

        # Update RECT
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    # New image function
    def new_image(self, file):
        # Load new image
        self.image = pg.image.load(file).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.scale_x, self.scale_y))
        self.image = pg.transform.rotate(self.image, self.angle)