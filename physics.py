"""module that implements obvious rules of physics"""
import pygame
import math
import time


def gravity(entity, objects, screen):
    stand = 0
    objects = objects.copy()
    objects.remove(entity)
    
    support1 = (entity.get_x()+1,entity.get_y()+entity.get_height())
    support2 = (entity.get_x()+entity.get_width()-1,entity.get_y() + entity.get_height())
    for object in objects:
        if object.get_rigid().collidepoint(support1) or object.get_rigid().collidepoint(support2):
            stand+=1
    if stand == 0 and entity.alive:
        entity.fall()
        if entity.direction == 'right':
            screen.move_background(10)
            for object in objects:
                object.move(10)
            pygame.time.delay(15)
        if entity.direction == 'left':
            screen.move_background(-10)
            for object in objects:
                object.move(-10)
            pygame.time.delay(15)

    return stand
    
def stutter(entity, objects):
    left_wall = 0
    right_wall = 0
    objects = objects.copy()
    objects.remove(entity)

    support_left1 = (entity.get_x(), entity.get_y() + 10)
    support_left2 = (entity.get_x(), entity.get_y() + entity.get_height() - 10)
    support_right1 = (entity.get_x() + entity.get_width(), entity.get_y() + 10)
    support_right2 = (entity.get_x() + entity.get_width(), entity.get_y() + entity.get_height() - 10)

    for object in objects:
        if object.get_rigid().collidepoint(support_left1) or object.get_rigid().collidepoint(support_left2):
            left_wall = 1
        if object.get_rigid().collidepoint(support_right1) or object.get_rigid().collidepoint(support_right2):
            right_wall = 1

    return [left_wall, right_wall]
