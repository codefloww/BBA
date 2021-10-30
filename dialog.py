"""A module to work with dialogs"""
import pygame as pg
import main


class Dialog:
    def __init__(self, width, height, back='Assets/red_square.png'):
        self.width = width
        self.height = height
        self.back = back

    def show_dial(self):
        self.texture = pg.Surface((self.width, self.height))
        self.texture = pg.transform.scale(
            pg.image.load('Assets/space.png'), (self.width, self.height)
        )
        screen.blit(self.texture, (main.player.get_x(),
                    main.player.get_y()))


screen = pg.display.set_mode((1920, 1080))

dialog = Dialog(400, 200)
dialog.show_dial()
pg.display.update()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
