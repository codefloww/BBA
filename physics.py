"""module that implements obvious rules of physics"""
import pygame
import math
import time


def gravity(entity, objects):
    stand = 0
    objects = objects.copy()
    objects.remove(entity)
    
    support1 = (entity.x+1,entity.y+entity.height)
    support2 = (entity.x+entity.width-1,entity.y + entity.height)
    for object in objects:
        if object.get_rigid().collidepoint(support1) or object.get_rigid().collidepoint(support2):
            stand+=1
    if stand == 0:
        entity.fall()
        if entity.direction == 'right':
            entity.x += 5
            pygame.time.delay(15)
        if entity.direction == 'left':
            entity.x -= 5
            pygame.time.delay(15)

    return stand 