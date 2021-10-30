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
    """class to work with window properties"""

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
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", background)),
            (self.width, self.height),
        )

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
            self.screen.blit(object.get_image(),
                             (object.get_x(), object.get_y()))
        pygame.display.update()

    def get_background(self):
        return self.background

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


class Player:
    """class to specify player's attributes"""

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
        self.direction = None
        self.stand = 0
        self.alive = True
    def get_health(self):
        return self.health
        
    def get_bowe(self):
        return self.bowe

    def get_state(self):
        return self.state

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
        """changes state of player"""
        self.state = "Human" if self.state == "Wolf" else "Wolf"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def fall(self):
        if self.get_y() > 1080:
            self.alive = False
        else:
            self.y += 5

    def jump(self, objects, screen):
        objects_unmoveable = objects.copy()
        objects_unmoveable.remove(self)
        if self.state == 'Wolf':
            delta = 150
            starting_y = self.get_y()
            if self.direction == 'right':
                t = 0
                while delta > 0:
                    self.y = starting_y + (1 * t * (t - 20))
                    t += 1
                    screen.move_background(15)
                    for object in objects_unmoveable:
                        object.move(15)
                    pygame.time.delay(15)
                    delta -= 15
                    screen.update_screen(objects)
            elif self.direction == 'left':
                t = 0
                while delta > 0:
                    self.y = starting_y + (1 * t * (t - 20))
                    t += 1
                    screen.move_background(-15)
                    for object in objects_unmoveable:
                        object.move(-15)
                    pygame.time.delay(15)
                    delta -= 15
                    screen.update_screen(objects)
            elif self.direction == None:
                t = 0
                while delta > 0:
                    self.y = starting_y + (1 * t * (t - 20))
                    t += 1
                    pygame.time.delay(15)
                    delta -= 15
                    screen.update_screen(objects)

        elif self.state == 'Human':
            self.y -= 5

    def movement_handle(self, keys_pressed, objects, stand, screen):
        objects_unmoveable = objects.copy()
        objects_unmoveable.remove(self)
        if self.state == 'Wolf':
            if keys_pressed[pygame.K_RIGHT]:
                pygame.time.delay(15)
                screen.move_background(10)
                self.direction = 'right'
                for object in objects_unmoveable:
                    object.move(10)

            if keys_pressed[pygame.K_LEFT]:
                pygame.time.delay(15)
                screen.move_background(-10)
                self.direction = 'left'
                for object in objects_unmoveable:
                    object.move(-10)
            
            if keys_pressed[pygame.K_UP]:
                pygame.time.delay(15)
                if stand == 1:
                        stand = 0
                        self.jump(objects,screen)
                        screen.update_screen(objects)

class Human(Player):
    """class to specify human's part of the main charecter

    Args:
        Player (parent class)
    """

    def __init__(self, x, y, health, bowe, state) -> None:
        """initializes human properties"""
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

    def get_x(self):
        """Returns x coordinate of human"""
        return self.x

    def get_y(self):
        """Returns y coordinate of human"""
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_image(self):
        """Returns texture of human"""
        return self.texture

    def get_rigid(self):
        return self.rigid



class Wolf(Player):
    """class to specify wolf's part of the main charecter

    Args:
        Player (parent class)
    """

    def __init__(self, x, y, health, bowe, state) -> None:
        super().__init__(x, y, health, bowe, state)
        self.velocity = 5
        self.mass = 5
        self.width = 100
        self.height = 100
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "wolf_standing.png")),
            (self.width * 1.15, self.height * 1.15),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_image(self):
        return self.texture

    def get_rigid(self):
        return self.rigid

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Story:
    def __init__(self) -> None:
        pass


class Mobs:
    def __init__(self) -> None:
        pass


class Road:
    """class to build paths and solid ground in generall"""

    def __init__(self, x, y, type, width, height, texture="green_square.png") -> None:
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
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", texture)),
            (self.width, self.height),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

    def get_x(self):
        """returns x coordinate of block"""
        return self.x

    def get_y(self):
        """returns y coordinate of block"""
        return self.y

    def get_width(self):
        """returns width of block"""
        return self.width

    def get_height(self):
        """returns height of block"""
        return self.height

    def get_image(self):
        """returns texture of an block"""
        return self.texture

    def get_rigid(self):
        return self.rigid

    def move(self, vel):
        """Implementation of parallax effect, moves bg instead of player

        Args:
            vel (int): player's velocity
        """
        self.x -= vel
        self.rigid = self.rigid.move(-1 * vel, 0)


# class Items:
#     def __init__(self) -> None:
#         pass
#     def get_rigid(self):
#         return self.rigid
#     def get_image(self):
#         return self.image


class Button:
    def __init__(self, width, height, background, x, y, caption) -> None:
        self.width = width
        self.height = height
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", background)),
            (self.width, self.height),
        )
        self.x = x
        self.y = y
        self.state = "inactive"
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)
        self.caption = caption

    def get_rigid(self):
        return self.rigid

    def clicked(self, clicked_image):
        self.state = "active"
        self.background = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", clicked_image)),
            (self.width, self.height),
        )

    def get_image(self):
        return self.background

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_caption(self):
        return self.caption


"""Game's starting session"""
if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    menu = main_window.menu()
    if menu == 'PLAY':
        alive = False
        while alive == False:
            alive = stage1.stage()
    elif menu =='ABOUT US':
        print('here we are')



    

    