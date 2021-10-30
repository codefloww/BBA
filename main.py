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

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def fall(self):
        self.y += 5
    
    def jump(self):
        if self.state == 'Wolf':
            delta = 150
            while delta > 0:
                self.y -= 15
                pygame.time.delay(10)
                delta -= 15
                menu.update_screen(objects)
        elif self.state == 'Human':
            self.y -= 50


class Human(Player):
    """class to specify human's part of the main charecter

    Args:
        Player (parent class)
    """
    def __init__(self, x, y, health, bowe, state) -> None:
        """initializes human properties
        """
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
        self.texture = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", texture)),
            (self.width, self.height),
        )
        self.rigid = pygame.Rect(self.x, self.y, self.width, self.height)

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

    def get_rigid(self):
        return self.rigid

    def move_road(self, vel):
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


class Buttons:
    def __init__(self) -> None:
        pass

'''Game's starting session'''
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
    soil1 = Road(100, 500, "ground", 300, 100)
    soil2 = Road(300, 400, 'ground', 300, 100)
    objects.append(soil1)
    objects.append(soil2)
    objects_unmoveable = objects.copy()
    objects_unmoveable.remove(player)
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
                    menu.move_background(-10)
                    for object in objects_unmoveable:
                        object.move_road(-10)
                        object.get_rigid().move(-10, 0)
                if event.key == pygame.K_RIGHT:
                    menu.move_background(10)
                    for object in objects_unmoveable:
                        object.move_road(10)
                        object.get_rigid().move(10, 0)
                if event.key == pygame.K_UP:
                    if stand == 1:
                        player.jump()
                        menu.update_screen(objects)
                        stand = 0
        for entity in moveable:
            menu.update_screen(objects)
            # physics.gravity(entity, objects)
            stand = 0
            # objects_unmoveable = objects.copy()
            # objects_unmoveable.remove(entity)

            while stand == 0:
                support1 = (entity.get_x() + 1, entity.get_y() + entity.height)
                support2 = (
                    entity.get_x() + entity.width - 1,
                    entity.get_y() + entity.height,
                )
                #print(support1)
                for object in objects_unmoveable:
                    if object.get_rigid().collidepoint(
                        support1
                    ) or object.get_rigid().collidepoint(support2):
                        stand += 1
                if stand == 0:
                    entity.fall()
                    pygame.time.delay(5)
                    menu.update_screen(objects)
            
        menu.update_screen(objects)
