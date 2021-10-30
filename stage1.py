import main
import os
import pygame
pygame.mixer.init()
def stage():
    stage1 = main.Window(1920, 1080, "Beholder.mp3", "space.png")
    stage1.play_audio("start")
    running = True
    objects = []
    moveable = []
    player = main.Wolf(100, 100, 100, 10, "Wolf")
    moveable.append(player)
    objects.append(player)
    soil1 = main.Road(100, 500, "ground", 5000, 50)
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
                if event.key == pygame.K_UP:
                    if stand == 1:
                        stand = 0
                        player.jump(objects_unmoveable,stage1)
                        stage1.update_screen(objects)
                        
        for entity in moveable:
            stage1.update_screen(objects)
            # physics.gravity(entity, objects)
            stand = 0
            # objects_unmoveable = objects.copy()
            # objects_unmoveable.remove(entity)

            while stand == 0:
                support1 = (entity.get_x() + 1, entity.get_y() + entity.get_height())
                support2 = (
                    entity.get_x() + entity.get_width() - 1,
                    entity.get_y() + entity.get_height(),
                )
                # print(support1)
                for object in objects_unmoveable:
                    if object.get_rigid().collidepoint(
                        support1
                    ) or object.get_rigid().collidepoint(support2):
                        stand += 1
                if stand == 0:
                    entity.fall()
                    if entity.direction == 'right':
                        entity.x += 5
                        pygame.time.delay(15)
                    if entity.direction == 'left':
                        entity.x -= 5
                        pygame.time.delay(15)
                    stage1.update_screen(objects)
            
        keys_pressed = pygame.key.get_pressed()
        player.movement_handle(keys_pressed, objects_unmoveable, stand,stage1)

        stage1.update_screen(objects)

if __name__ == '__main__':
    stage()