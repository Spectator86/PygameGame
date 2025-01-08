import pygame as pg
from settings import *

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

while True:
    sc.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    clock.tick(FPS)
    pg.display.update()
