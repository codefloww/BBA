import main
import os
import pygame
import physics

pygame.mixer.init()
pygame.font.init()


def path(objects):
    k=1
    length = main.Road(k, 1000, "ground", 17000, 100, "ground.png")
    objects.append(length)
    k+=500

    sail1 = main.Road(k, 900, "ground", 150, 100, "ground.png")
    objects.append(sail1)
    k+=300
    sail2 = main.Road(k, 800, "ground", 150, 100, "ground.png")
    objects.append(sail2)

def stage():
    stage1 = main.Window(1920, 1080, "Oles.mp3", "background1.jpg")
    stage1.play_audio("start")
    running = True
    objects = []
    moveable = []  # Each moveable object, basically mobs and player
    player = main.Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    path(objects)

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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.running_animation = False
                if event.key == pygame.K_UP:
                    player.jumping_animation = False

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

        player.standing_animation = (not player.running_animation) & (not player.jumping_animation)
        if player.standing_animation:
            player.animate_stand(0.05)

        if not player.alive:
            running = False
            return player.alive


if __name__ == "__main__":
    stage()
