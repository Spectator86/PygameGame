import pygame as pg
from settings import *
from player import Player

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game")

clock = pg.time.Clock()

player = Player(10, WIDTH//2, HEIGHT//2, 100, 100, "images/player/player.png")

while True:
    sc.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    player.draw(sc)
    player.move()
    
    clock.tick(FPS)
    pg.display.update()
