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
    """class to work with window properties
    """
    def __init__(self, width, height, audio, background) -> None:
        """initializes window properties

        Args:
            width (int)
            height (int)
            audio (str): name of the audio file in Assets directory
            background (str): name of the background image file in Assets directory
        """
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.audio = pygame.mixer.music.load(os.path.join("Assets", audio))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", background)),(self.width,self.height))
        self.objects = []

    def get_size(self):
        """
        Returns:
            [tuple]: tuple of window's width and height
        """
        return (self.width, self.height)

    def update_screen(self, objects=[]):
        """updates screen for each object in objects list

        Args:
            objects (list, optional): list of objects. Defaults to [].
        """
        self.screen.blit(self.background, (self.x, self.y))
        for object in objects:
            self.screen.blit(object.get_image(), (object.get_x(), object.get_y()))
        pygame.display.update()

    def move_background(self, vel):
        """Implementation of parallax effect, moves bg instead of player

        Args:
            vel (int): player's velocity
        """
        self.x -= vel

    def play_audio(self, action):
        """gives abillity to manipulate music on the level

        Args:
            action (str): either start, play or stop
        """
        if action == "play":
            pygame.mixer.music.unpause()
        elif action == "stop":
            pygame.mixer.music.pause()
        elif action == "start":
            pygame.mixer.music.play(-1)

    def add_object(self, object):
        """adds object to object list in window class

        Args:
            object (): any object
        """
        self.objects.append(object)


class Player:
    """class to specify player's attributes
    """
    def __init__(self, x, y, health, bowe, state) -> None:
        """Initializes player's properties

        Args:
            x (int): x coordinate of player
            y (int): y coordinate of player
            health (int): health of a player
            bowe (int): level of bar of wolf energy
            state (str): player's state, either 'human' or 'wolf'
        """
        self.health = health
        self.bowe = bowe
        self.state = state
        self.x = x
        self.y = y

    def change_health(self, change):
        """changes player's health

        Args:
            change (int): value of change
        """
        self.health += change

    def change_bowe(self, change):
        """changes level of bowe

        Args:
            change (int): value of change
        """
        self.bowe += change

    def change_state(self):
        """changes state of player
        """
        self.state = "Human" if self.state == "Wolf" else "Wolf"


class Human(Player):
    """class to specify human's part of the main charecter

    Args:
        Player (parent class)
    """
    def __init__(self) -> None:
        """initializes human properties
        """
        self.velocity = 5
        self.mass = 5
        self.width = 100
        self.height = 100
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "space.png")),
            (self.width, self.height))
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_x(self):
        """Returns x coordinate of human
        """
        return self.x

    def get_y(self):
        """Returns y coordinate of human
        """
        return self.y

    def get_image(self):
        """Returns texture of human
        """
        return self.texture


class Wolf(Player):
    """class to specify wolf's part of the main charecter

    Args:
        Player (parent class)
    """
    def __init__(self) -> None:
        pass


class Story:
    def __init__(self) -> None:
        pass


class Mobs:
    def __init__(self) -> None:
        pass


class Road:
    """class to build paths and solid ground in generall
    """
    def __init__(self, x, y, type, width, height, texture = 'green_square.png') -> None:
        """initializes road block properties

        Args:
            x (int): x coordinate of block
            y (int): y coordinate of block
            type (str): type of road
            width (int): width of road
            height (int): height of block
            texture (str, optional): name of texture's file in Assets directory. Defaults to 'green_square.png'.
        """
        self.x = x
        self.y = y
        self.type = type
        self.width = width
        self.height = height
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join('Assets', texture)), (self.width, self.height))
        self.body = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_x(self):
        """returns x coordinate of block
        """
        return self.x

    def get_y(self):
        """returns y coordinate of block
        """
        return self.y

    def get_width(self):
        """returns width of block
        """
        return self.width

    def get_height(self):
        """returns height of block
        """
        return self.height

    def get_image(self):
        """returns texture of an block
        """
        return self.texture


class Items:
    def __init__(self) -> None:
        pass


class Buttons:
    def __init__(self) -> None:
        pass

'''Game's starting session'''
if __name__ == "__main__":
    pygame.init()
    menu = Window(1920, 1080, "Beholder.mp3", "space.png")
    menu.play_audio("start")
    running = True
    while running:
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
        menu.update_screen()
