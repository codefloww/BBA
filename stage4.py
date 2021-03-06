import main
import os
import pygame
import physics

pygame.mixer.init()


def stage():
    stage4 = main.Window(1920, 1080, "Enter.mp3", "background4.jpg")
    stage4.play_audio("start")
    running = True
    objects = []
    moveable = []  # Each moveable object, basically mobs and player
    player = main.Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    soil1 = main.Road(100, 500, "ground", 900, 50)
    soil2 = main.Road(300, 400, "ground", 100, 100)
    objects.append(soil1)
    objects.append(soil2)
    objects_unmoveable = objects.copy()
    objects_unmoveable.remove(player)
    clock = pygame.time.Clock()

    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    stage4.play_audio("stop")
                if event.key == pygame.K_p:
                    stage4.play_audio("play")

        for entity in moveable:
            stage4.update_screen(objects)
            # physics.gravity(entity, objects)
            stand = 0
            wall_collision = physics.stutter(entity, objects)

            while stand == 0 and entity.alive:
                stand = physics.gravity(entity, objects, stage4)
                entity.direction = None
                stage4.update_screen(objects)
        keys_pressed = pygame.key.get_pressed()
        player.movement_handle(keys_pressed, objects, stand, stage4, wall_collision)
        stage4.update_screen(objects)

        if not player.alive:
            running = False
            return player.alive


if __name__ == "__main__":
    stage()
