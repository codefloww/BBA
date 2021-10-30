import main
import pygame
import os


def menu():
    pygame.mixer.init()
    main_menu = main.Window(1920, 1080, "Oles.mp3", "space.png")
    main_menu.play_audio("start")
    running = True
    objects = []
    BUTTON_PLAY = main.Button(200, 100, "space.png", 860, 400, "PLAY")
    BUTTON_EXIT = main.Button(200, 100, "space.png", 860, 550, "EXIT")
    BUTTON_ABOUT_US = main.Button(200, 100, "space.png", 860, 700, "ABOUT US")
    objects.append(BUTTON_PLAY)
    objects.append(BUTTON_EXIT)
    objects.append(BUTTON_ABOUT_US)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in objects:
                        if button.get_rigid().collidepoint(pos):
                            button.clicked("space.png")
                            running = False
                            return button.get_caption()

        main_menu.update_screen(objects)
        pygame.display.update()


if __name__ == "__main__":
    print(menu())
