import main
import os
import pygame
import physics

pygame.mixer.init()
pygame.font.init()


def path(objects):
    k=1
    length = main.Road(k, 1000, "ground", 4000, 100, "ground.png")
    objects.append(length)
    length = main.Road(4151, 1000, "ground", 1800, 100, "ground.png")
    objects.append(length)
    k+=1000

    sail1 = main.Road(k, 905, "ground", 150, 100, "ground.png")
    objects.append(sail1)
    k+=1200
    sail1 = main.Road(k, 905, "ground", 150, 100, "ground.png")
    objects.append(sail1)
    k+=300
    sail2 = main.Road(k, 805, "ground", 150, 100, "ground.png")
    objects.append(sail2)

    k+=1200
    sail1 = main.Road(k, 905, "ground", 150, 100, "ground.png")
    objects.append(sail1)
    k+=300
    sail2 = main.Road(k, 805, "ground", 150, 100, "ground.png")
    objects.append(sail2)
    k+=1000

    # сюди моба. на к координату по х
    
    k+=1000
    sail1 = main.Road(k, 905, "ground", 200, 100, "ground.png")
    objects.append(sail1)
    k+=301
    sail2 = main.Road(k, 805, "ground", 200, 100, "ground.png")
    objects.append(sail2)
    k+=301
    sail1 = main.Road(k, 705, "ground", 200, 100, "ground.png")
    objects.append(sail1)
    k+=301
    sail2 = main.Road(k, 605, "ground", 200, 100, "ground.png")
    objects.append(sail2)
    k+=301
    sail2 = main.Road(k, 505, "ground", 900, 100, "ground.png")
    objects.append(sail2)
    k+=400
    # mob
    k+=700
    sail2 = main.Road(k, 505, "ground", 200, 100, "ground.png")
    objects.append(sail2)
    k+=350
    sail1 = main.Road(k, 605, "ground", 200, 100, "ground.png")
    objects.append(sail1)
    k+=351
    sail2 = main.Road(k, 705, "ground", 200, 100, "ground.png")
    objects.append(sail2)
    k+=351
    sail1 = main.Road(k, 805, "ground", 200, 100, "ground.png")
    objects.append(sail1)
    k+=351
    sail2 = main.Road(k, 905, "ground", 200, 100, "ground.png")
    objects.append(sail2)
    k+=350
    sail2 = main.Road(k, 1000, "ground", 6000, 100, "ground.png")
    objects.append(sail2)


def stage():
    stage1 = main.Window(1920, 1080, "Oles.mp3", "background1.jpg")
    stage1.play_audio("start")
    running = True
    objects = []
    moveable = []  # Each moveable object, basically mobs and player
    dialogable = [] # each object that we can have a dialog with
    mobs = []
    player = main.Human(700, 900, 100, 10, "Human")
    moveable.append(player)
    objects.append(player)
    # soil1 = main.Road(0, 500, "ground", 900, 50)
    # soil2 = main.Road(300, 400, "ground", 100, 300)
    # objects.append(soil1)
    # objects.append(soil2)
    priest = main.Mobs(1400, 920, 100, 80, "priest.png")
    priest.dialogable()
    objects.append(priest)
    mobs.append(priest)
    dialogable.append(priest)
    clock = pygame.time.Clock()
    path(objects)

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
                if event.key == pygame.K_d and player.dialog_possible(dialogable):
                    dial = main.Dialog(0)
                    dial.show_mob_dial(
                        "I was here since a long time ago", player, stage1
                    )
                if event.key == pygame.K_f:
                    player.hit(mobs)
                if event.key == pygame.K_t:
                     player.change_state()
                     player.animate_change_state(objects, stage1)
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
        for mob in mobs:
            if mob.get_health() < 0:
                mob.alive = False
        stage1.update_screen(objects)

        player.standing_animation = (not player.running_animation) & (
            not player.jumping_animation
        )
        if player.standing_animation:
            player.animate_stand(0.05)

        for mob in mobs:
            if not mob.alive:
                mobs.remove(mob)
                dialogable.remove(mob)
                objects.remove(mob)
        if not player.alive:
            running = False
            return player.alive


if __name__ == "__main__":
    stage()
