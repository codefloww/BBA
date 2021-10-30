import main
import os
import pygame
import physics
pygame.mixer.init()
def stage():
    alive = True
    stage1 = main.Window(1920, 1080, "Beholder.mp3", "space.png")
    stage1.play_audio("start")
    running = True
    objects = []
    moveable = []  # Each moveable object, basically mobs and player
    player = main.Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    soil1 = main.Road(100, 500, "ground", 500, 50)
    soil2 = main.Road(300, 400, "ground", 100, 100)
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
                    stage1.play_audio("stop")
                if event.key == pygame.K_p:
                    stage1.play_audio("play")

        for entity in moveable:
            stage1.update_screen(objects)
            # physics.gravity(entity, objects)
            stand = 0
            objects_unmoveable = objects.copy()
            objects_unmoveable.remove(entity)

            while stand == 0 and entity.alive:
                stand = physics.gravity(entity, objects, stage1)
                entity.direction = None
                stage1.update_screen(objects)
        keys_pressed = pygame.key.get_pressed()
        player.movement_handle(keys_pressed, objects, stand, stage1)
        stage1.update_screen(objects)

        if not player.alive:
            running = False
            return player.alive


if __name__ == '__main__':
    stage()