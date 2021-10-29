"""module that maintains full game"""
import time
import os
import main_window
import stage1
import stage2
import stage3
import stage4
import pygame


class Window:
    def __init__(self, width, height, audio, background) -> None:
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.audio = pygame.mixer.music.load(os.path.join("Assets", audio))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", background)), (self.width, self.height))

    def get_size(self):
        return (self.width,self.height)

    def update_screen(self, objects):
        self.screen.blit(self.background,(self.x,self.y))
        for object in objects:
            self.screen.blit(object.get_image(),(object.x,object.y))
        pygame.display.update()

    def move_background(self,vel):
        self.x-=vel

    def play_audio(self):
        pygame.mixer.music.play(-1)


class Player:
    def __init__(self) -> None:
        pass


class Human:
    def __init__(self) -> None:
        pass


class Wolf:
    def __init__(self) -> None:
        pass


class Story:
    def __init__(self) -> None:
        pass


class Mobs:
    def __init__(self) -> None:
        pass


class Road:
    def __init__(self, x, y, type, width, height, texture = 'green_square.png') -> None:
        self.x = x
        self.y = y
        self.type = type
        self.width = width
        self.height = height
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join('Assets', texture)), (self.width, self.height))
        self.body = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.texture


class Items:
    def __init__(self) -> None:
        pass


class Buttons:
    def __init__(self) -> None:
        pass


if __name__=="__main__":
    pygame.init()
    menu = Window(1920,1080,'Beholder.mp3','space.png')
    menu.play_audio()
    running = True
    objects = []
    trip = Road(100, 100, 'ground', 100, 10)
    menu.screen.blit(trip.get_image(), (trip.x, trip.y))
    objects.append(trip)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    menu.move_background(10)
                if event.key == pygame.K_RIGHT:
                    menu.move_background(-10)
        menu.update_screen(objects)