"""module that maintains full game"""
import time
import os
import main_window
import stage1
import stage2
import stage3
import stage4
import pygame
import physics


class Window:
    def __init__(self, width, height, audio, background) -> None:
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.audio = pygame.mixer.music.load(os.path.join("Assets", audio))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", background)),
            (self.width, self.height),
        )

    def get_size(self):
        return (self.width, self.height)

    def update_screen(self, objects=[]):
        self.screen.blit(self.background, (self.x, self.y))
        for object in objects:
            self.screen.blit(object.get_image(), (object.get_x(), object.get_y()))
        pygame.display.update()

    def move_background(self, vel):
        self.x -= vel

    def play_audio(self, action):
        if action == "play":
            pygame.mixer.music.unpause()
        elif action == "stop":
            pygame.mixer.music.pause()
        elif action == "start":
            pygame.mixer.music.play(-1)


class Player:
    def __init__(self, x, y, health, bowe, state) -> None:
        self.health = health
        self.bowe = bowe
        self.state = state
        self.x = x
        self.y = y

    def change_health(self, change):
        self.health += change

    def change_bowe(self, change):
        self.bowe += change

    def change_state(self):
        self.state = "Human" if self.state == "Wolf" else "Wolf"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def fall(self):
        self.y += 5


class Human(Player):
    def __init__(self, x, y, health, bowe, state) -> None:
        super().__init__(x, y, health, bowe, state)
        self.velocity = 5
        self.mass = 5
        self.width = 100
        self.height = 100
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "space.png")),
            (self.width, self.height),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_image(self):
        return self.texture

    def get_rigid(self):
        return self.rigid


class Wolf(Player):
    def __init__(self, x, y, health, bowe, state) -> None:
        super().__init__(x, y, health, bowe, state)
        self.velocity = 5
        self.mass = 5
        self.width = 100
        self.height = 100
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "wolf_standing.png")),
            (self.width, self.height),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_image(self):
        return self.texture

    def get_rigid(self):
        return self.rigid


class Story:
    def __init__(self) -> None:
        pass


class Mobs:
    def __init__(self) -> None:
        pass


class Road:
    def __init__(self, x, y, type, width, height, texture="green_square.png") -> None:
        self.x = x
        self.y = y
        self.type = type
        self.width = width
        self.height = height
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", texture)),
            (self.width, self.height),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.texture

    def get_rigid(self):
        return self.rigid


# class Items:
#     def __init__(self) -> None:
#         pass
#     def get_rigid(self):
#         return self.rigid
#     def get_image(self):
#         return self.image


class Buttons:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    pygame.init()
    menu = Window(1920, 1080, "Oles.mp3", "space.png")
    menu.play_audio("start")
    running = True
    objects = []
    moveable = []
    player = Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    soil = Road(100, 500, "ground", 100, 100)
    objects.append(soil)
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    menu.play_audio("stop")
                if event.key == pygame.K_p:
                    menu.play_audio("play")
                if event.key == pygame.K_LEFT:
                    menu.move_background(10)
                if event.key == pygame.K_RIGHT:
                    menu.move_background(-10)
        for entity in moveable:
            menu.update_screen(objects)
            # physics.gravity(entity, objects)
            stand = 0
            objects1 = objects.copy()
            objects1.remove(entity)

            while stand == 0:
                support1 = (entity.get_x() + 1, entity.get_y() + entity.height)
                support2 = (
                    entity.get_x() + entity.width - 1,
                    entity.get_y() + entity.height,
                )
                print(support1)
                for object in objects1:
                    if object.get_rigid().collidepoint(
                        support1
                    ) or object.get_rigid().collidepoint(support2):
                        stand += 1
                if stand == 0:
                    entity.fall()
                    pygame.time.delay(5)
                    menu.update_screen(objects)
        menu.update_screen(objects)
