import main
import pygame
import os


def menu():
    pygame.mixer.init()
    main_menu = main.Window(1920, 1080, "Enter.mp3", "background.jpg")
    main_menu.play_audio("start")
    running = True
    objects = []
    BUTTON_IMAGES = {'PLAY':('startgame1.jpg','startgame2.jpg'),'EXIT':('exit1.jpg','exit2.jpg'),'ABOUTUS':('aboutus1.jpg','aboutus2.jpg')}
    BUTTON_PLAY = main.Button(200, 100, BUTTON_IMAGES["PLAY"][0], 860, 400, "PLAY")
    BUTTON_EXIT = main.Button(200, 100, BUTTON_IMAGES["EXIT"][0], 860, 550, "EXIT")
    BUTTON_ABOUT_US = main.Button(200, 100,BUTTON_IMAGES["ABOUTUS"][0], 860, 700, "ABOUTUS")
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
                            button.clicked(BUTTON_IMAGES[button.get_caption()][1],main_menu)
                            running = False
                            return button.get_caption()

        clock = pygame.time.Clock()
        clock.tick(120)
        if 1:
            pygame.time.delay(1)
            main_menu.move_background(0.5)

        main_menu.update_screen(objects)


if __name__ == "__main__":
    print(menu())
