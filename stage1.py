import main
import os
import pygame
import physics

pygame.mixer.init()
pygame.font.init()


def stage():
    stage1 = main.Window(1920, 1080, "Oles.mp3", "background1.jpg")
    stage1.play_audio("start")
    running = True
    objects = []
    moveable = []  # Each moveable object, basically mobs and player
    player = main.Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    soil1 = main.Road(100, 500, "ground", 900, 50)
    soil2 = main.Road(300, 400, "ground", 100, 300)
    objects.append(soil1)
    objects.append(soil2)

    clock = pygame.time.Clock()
    while running:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    stage1.play_audio("stop")
                if event.key == pygame.K_p:
                    stage1.play_audio("play")
                if event.key == pygame.K_d:
                    dial = main.Dialog(0)
                    dial.show_mob_dial(
                        "I was here since a long time ago", player, stage1
                    )

        for entity in moveable:
            stage1.update_screen(objects)
            stand = 0
            wall_collision = physics.stutter(entity, objects)

            while stand == 0 and entity.alive:
                stand = physics.gravity(entity, objects, stage1)
                entity.direction = None
                stage1.update_screen(objects)

        keys_pressed = pygame.key.get_pressed()
        player.movement_handle(keys_pressed, objects, stand, stage1, wall_collision)
        stage1.update_screen(objects)

        if not player.alive:
            running = False
            return player.alive


if __name__ == "__main__":
    stage()
